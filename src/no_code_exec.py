import os
from autogen import AssistantAgent, UserProxyAgent

# if we speak with MS Azure Open AI, then following five keys are needed
llm_config = {
    "model": os.getenv('autogen_model'), 
    "api_key": os.getenv('autogen_api_key'), 
    "base_url": os.getenv('autogen_base_url'),
    "api_type": os.getenv('autogen_api_type'),
    "api_version": os.getenv('autogen_api_version')
    }
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)