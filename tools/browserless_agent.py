from dify_plugin import Tool

from tools._base import BrowserlessMCPMixin


class BrowserlessAgentTool(BrowserlessMCPMixin, Tool):
    mcp_tool_name = "browserless_agent"
    json_param_keys = ('params', 'commands')
