import os

from autogen import ConversableAgent

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="You are playing a game of guess-my-number. You have the "
    "number 41 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
    llm_config={"config_list": [{"model": os.getenv('autogen_model'), 
                "api_key": os.getenv('autogen_api_key'), 
                "base_url": os.getenv('autogen_base_url'),
                "api_type": os.getenv('autogen_api_type'),
                "api_version": os.getenv('autogen_api_version')}]},
    is_termination_msg=lambda msg: "41" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config={"config_list": [{"model": os.getenv('autogen_model'), 
                "api_key": os.getenv('autogen_api_key'), 
                "base_url": os.getenv('autogen_base_url'),
                "api_type": os.getenv('autogen_api_type'),
                "api_version": os.getenv('autogen_api_version')}]},
    human_input_mode="NEVER",
)

result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)