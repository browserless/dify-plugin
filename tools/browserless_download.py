from tools._base import BrowserlessMCPTool


class BrowserlessDownloadTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_download"
    json_param_keys = ('context',)
