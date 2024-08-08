import os

from autogen import ConversableAgent

cathy = ConversableAgent(
    "Kasia",
    system_message="Your name is Kasia and you are a part of a duo of comedians.",
    #llm_config={"config_list": [{"model": "gpt-4", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    llm_config={"config_list": [{"model": os.getenv('autogen_model'), 
                "api_key": os.getenv('autogen_api_key'), 
                "base_url": os.getenv('autogen_base_url'),
                "api_type": os.getenv('autogen_api_type'),
                "api_version": os.getenv('autogen_api_version'), 
                "temperature": 0.9}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "jacuś",
    system_message="Your name is Jacuś and you are a part of a duo of comedians.",
    llm_config={"config_list": [{"model": os.getenv('autogen_model'), 
                "api_key": os.getenv('autogen_api_key'), 
                "base_url": os.getenv('autogen_base_url'),
                "api_type": os.getenv('autogen_api_type'),
                "api_version": os.getenv('autogen_api_version'), 
                "temperature": 0.7}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Kasiu, może mi opowiesz żarcik o zwierzątkach?", max_turns=3)