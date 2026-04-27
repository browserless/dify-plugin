from tools._base import BrowserlessMCPTool


class BrowserlessPerformanceTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_performance"
    json_param_keys = ('categories', 'budgets')
