# Program demonstruje użycie funkcji, których agenci autonomiczni mogą użyć (o ile tak zdecydują)
#
# Mamy dwie funkcje:
#   - jedna dostarcza informacji na temat fikcyjnego urządzenia zwanego turboglobulator
#   - druga dostarcza informacji na temat odkrywcy turboglobulatora
#
# ***************************
# Jeśli to samo chcemy przećwiczyć w AutogenStudio UI, to trzeba się odrobinkę nagimnastykować
#   - utworzyć dwa skille (jeden skill odpowiada jednej funkcji zdefiniowanej w fct_functions_in_autogen.py)
#   - uwtworzyć po jednym agencie (assistant) dla skilla, agentowi pozwolić na wykonywanie kodu, 
#       do agenta dodać model gpt-4-turbo (lub wyższy)
#   - jeśli skill potrzebuje coś przeliczyć na podstawie zmiennych środowiskowych, to ustawić je w .env 
#       i załadować w każdym skillu osobno
#   - utworzyć agenta typu group_chat, dodać do niego agenty w/w
#   - zrobić workflow autonomiczny, inicjatorem będzie user_proxy, drugim rozmówcą będzie group_chat
#       (który koordynuje pracę agentów odpowiedzialnych za wywoływanie skilli)
#
import os
from autogen import ConversableAgent
# from typing import Annotated, Literal
from autogen import register_function
from fct_functions_in_autogen import f_turboglob_data, f_turboglob_inventor
    
# Let's first define the assistant agent that suggests tool calls.
turbog_assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    #"You can help with simple calculations. "
    "You are a specialist in crude oil processing technologies. "
    "You can create your answers based on all knowledge you have. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={"config_list": [{"model": os.getenv('autogen_model'), 
    "api_key": os.getenv('autogen_api_key'), 
    "base_url": os.getenv('autogen_base_url'),
    "api_type": os.getenv('autogen_api_type'),
    "api_version": os.getenv('autogen_api_version')}]},
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
turbog_user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
turbog_assistant.register_for_llm(
    name="f_turboglob_data", 
    description="Information about turboglobulator"
    )(f_turboglob_data)

turbog_assistant.register_for_llm(
    name="f_turboglob_inventor", 
    description="Information about turboglobulator inventor"
    )(f_turboglob_inventor)

# Register the tool function with the user proxy agent.
turbog_user_proxy.register_for_execution(name="f_turboglob_data")(f_turboglob_data)
turbog_user_proxy.register_for_execution(name="f_turboglob_inventor")(f_turboglob_inventor)

# Register the function provifing data related to turboglobulators.
register_function(
    f_turboglob_data,
    caller=turbog_assistant,  # The assistant agent can suggest calls to the function.
    executor=turbog_user_proxy,  # The user proxy agent can execute the function calls.
    name="f_turboglob_data",  # By default, the function name is used as the tool name.
    description="Information about turboglobulator",  # A description of the tool.
)

# Register the function provifing data related to turboglobulators.
register_function(
    f_turboglob_inventor,
    caller=turbog_assistant,  # The assistant agent can suggest calls to the function.
    executor=turbog_user_proxy,  # The user proxy agent can execute the function calls.
    name="f_turboglob_inventor",  # By default, the function name is used as the tool name.
    description="Information about turboglobulator inventor",  # A description of the tool.
)

chat_result = turbog_user_proxy.initiate_chat(
    turbog_assistant, message=
    "Who invented turboglobulator? "
    "I want to learn about a turboglobulator technology, when to use it. "
    "I want to become a technician maintaining turboglobulator. "
    "How to prepare for the work interview? "
    "I want to learn about the background, who invented turboglobulator, when, where are they used, are they safe?"
    )