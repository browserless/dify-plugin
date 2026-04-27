from typing import Any

import httpx
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class BrowserlessProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        api_key = (credentials or {}).get("api_key", "").strip()
        if not api_key:
            raise ToolProviderCredentialValidationError(
                "Browserless API token is required."
            )

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list",
            "params": {},
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }

        try:
            response = httpx.post(
                "https://mcp.browserless.io/mcp",
                headers=headers,
                json=payload,
                timeout=15.0,
            )
        except httpx.HTTPError as exc:
            raise ToolProviderCredentialValidationError(
                f"Could not reach Browserless MCP: {exc}"
            ) from exc

        if response.status_code in (401, 403):
            raise ToolProviderCredentialValidationError(
                "Browserless rejected the API token. Sign up at https://www.browserless.io/signup/email to get one."
            )
        if response.status_code >= 400:
            raise ToolProviderCredentialValidationError(
                f"Browserless MCP returned HTTP {response.status_code}: {response.text[:200]}"
            )
