from tools._base import BrowserlessMCPTool


class BrowserlessAgentTool(BrowserlessMCPTool):
    mcp_tool_name = "browserless_agent"
    json_param_keys = ('params', 'commands')
