from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessPerformanceTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_performance"
    json_param_keys = ('categories', 'budgets')
