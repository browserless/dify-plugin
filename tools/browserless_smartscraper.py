from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessSmartscraperTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_smartscraper"
    json_param_keys = ('formats',)
