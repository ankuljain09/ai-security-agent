from google.adk.agents import LlmAgent
from google.genai import types
from .tools import run_complete_security_scan
from .config import config

ATOMIC_AGENT_PROMPT = """
You are an AI Security Manager.
Your ONLY job is to use the `run_complete_security_scan` tool to test the system.

When a user gives you a vulnerability category:
1. Call `run_complete_security_scan` immediately.
2. Output the result provided by the tool.
3. Do not add your own commentary.
"""

root_agent = LlmAgent(
    name="security_orchestrator",
    model=config.critic_model,
    instruction=ATOMIC_AGENT_PROMPT,
    tools=[run_complete_security_scan],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.0
    )
)
