from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessSearchTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_search"
    json_param_keys = ('sources', 'categories', 'scrapeOptions')
