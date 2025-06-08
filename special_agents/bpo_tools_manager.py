from agents import Agent, WebSearchTool, ModelSettings
from utils import load_prompt, DISCLAIMER

default_model = "gpt-4.1"
default_search_context = "medium"
RECENT_DAYS = 15

def build_bpo_tools_manager_agent():
    tool_retry_instructions = load_prompt("tool_retry_prompt.md")
    fundamental_prompt = load_prompt("bpo_tools_manager_base.md", RECENT_DAYS=RECENT_DAYS)
    
    return Agent(
        name="PA BPO Tools Manager Agent",
        instructions=(fundamental_prompt + DISCLAIMER + tool_retry_instructions),
        mcp_servers=[],
        tools=[WebSearchTool(search_context_size=default_search_context)],
        model=default_model,
        model_settings=ModelSettings(parallel_tool_calls=True, temperature=0),
    ) 