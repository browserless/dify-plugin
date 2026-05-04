from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessExportTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_export"
    json_param_keys = ('gotoOptions',)
