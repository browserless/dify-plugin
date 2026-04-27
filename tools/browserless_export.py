from tools._base import BrowserlessMCPTool


class BrowserlessExportTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_export"
    json_param_keys = ('gotoOptions',)
