from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessMapTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_map"
    json_param_keys = ()
