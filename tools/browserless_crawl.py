from tools._base import BrowserlessMCPTool


class BrowserlessCrawlTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_crawl"
    json_param_keys = ('includePaths', 'excludePaths', 'scrapeOptions')
