from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessDownloadTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_download"
    json_param_keys = ('context',)
