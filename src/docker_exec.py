import os
import autogen
from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "model": os.getenv('autogen_model'), 
    "api_key": os.getenv('autogen_api_key'), 
    "base_url": os.getenv('autogen_base_url'),
    "api_type": os.getenv('autogen_api_type'),
    "api_version": os.getenv('autogen_api_version')
    }

with autogen.coding.DockerCommandLineCodeExecutor(work_dir="coding") as code_executor:
    assistant = AssistantAgent("assistant", llm_config=llm_config)
    user_proxy = UserProxyAgent(
        "user_proxy", code_execution_config={"executor": code_executor}
    )

    # Start the chat
    user_proxy.initiate_chat(
        assistant,
        message="Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png",
    )