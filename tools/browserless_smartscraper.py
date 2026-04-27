from tools._base import BrowserlessMCPTool


class BrowserlessSmartscraperTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_smartscraper"
    json_param_keys = ('formats',)
