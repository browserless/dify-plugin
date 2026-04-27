from tools._base import BrowserlessMCPTool


class BrowserlessFunctionTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_function"
    json_param_keys = ('context',)
