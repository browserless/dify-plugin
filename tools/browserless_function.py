from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessFunctionTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_function"
    json_param_keys = ('context',)
