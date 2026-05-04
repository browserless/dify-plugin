from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessCrawlTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_crawl"
    json_param_keys = ('includePaths', 'excludePaths', 'scrapeOptions')
