import json
from collections.abc import Generator
from typing import Any

import httpx
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

MCP_ENDPOINT = "https://mcp.browserless.io/mcp"


class BrowserlessMCPTool(Tool):
    """Base class for tools that proxy to the Browserless MCP server."""

    mcp_tool_name: str = ""
    json_param_keys: tuple[str, ...] = ()

    def _build_arguments(self, tool_parameters: dict[str, Any]) -> dict[str, Any]:
        arguments: dict[str, Any] = {}
        for key, value in tool_parameters.items():
            if value is None or value == "":
                continue
            if key in self.json_param_keys and isinstance(value, str):
                try:
                    arguments[key] = json.loads(value)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Parameter '{key}' must be valid JSON: {exc.msg}"
                    ) from exc
            else:
                arguments[key] = value
        return arguments

    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        api_key = self.runtime.credentials.get("api_key")
        if not api_key:
            raise ValueError("Missing Browserless API token in plugin credentials.")

        arguments = self._build_arguments(tool_parameters)
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": self.mcp_tool_name, "arguments": arguments},
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }

        try:
            with httpx.Client(timeout=httpx.Timeout(180.0, connect=15.0)) as client:
                response = client.post(MCP_ENDPOINT, headers=headers, json=payload)
        except httpx.HTTPError as exc:
            raise ValueError(f"Failed to reach Browserless MCP: {exc}") from exc

        if response.status_code >= 400:
            raise ValueError(
                f"Browserless MCP returned HTTP {response.status_code}: {response.text[:500]}"
            )

        envelope = _parse_jsonrpc(response)
        if "error" in envelope:
            err = envelope["error"]
            raise ValueError(
                f"Browserless MCP error ({err.get('code')}): {err.get('message')}"
            )

        result = envelope.get("result") or {}
        if result.get("isError"):
            text = _join_text(result.get("content") or [])
            raise ValueError(text or "Tool returned an error.")

        for block in result.get("content") or []:
            kind = block.get("type")
            if kind == "text":
                yield self.create_text_message(block.get("text") or "")
            elif kind == "image":
                data = block.get("data")
                mime = block.get("mimeType") or "image/png"
                if data:
                    yield self.create_blob_message(
                        blob=_b64decode(data), meta={"mime_type": mime}
                    )
            elif kind == "resource":
                resource = block.get("resource") or {}
                if "text" in resource:
                    yield self.create_text_message(resource["text"])
                elif "blob" in resource:
                    yield self.create_blob_message(
                        blob=_b64decode(resource["blob"]),
                        meta={"mime_type": resource.get("mimeType") or "application/octet-stream"},
                    )
            else:
                yield self.create_json_message(block)

        if result.get("structuredContent"):
            yield self.create_json_message(result["structuredContent"])


def _parse_jsonrpc(response: httpx.Response) -> dict[str, Any]:
    content_type = response.headers.get("content-type", "")
    body = response.text
    if "text/event-stream" in content_type:
        for line in body.splitlines():
            if line.startswith("data:"):
                data = line[5:].strip()
                if not data:
                    continue
                try:
                    return json.loads(data)
                except json.JSONDecodeError:
                    continue
        raise ValueError("Browserless MCP returned no parseable SSE event.")
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Browserless MCP returned invalid JSON: {exc.msg}") from exc


def _join_text(blocks: list[dict[str, Any]]) -> str:
    return "\n".join(b.get("text", "") for b in blocks if b.get("type") == "text")


def _b64decode(data: str) -> bytes:
    import base64

    return base64.b64decode(data)
