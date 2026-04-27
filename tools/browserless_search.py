from tools._base import BrowserlessMCPTool


class BrowserlessSearchTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_search"
    json_param_keys = ('sources', 'categories', 'scrapeOptions')
