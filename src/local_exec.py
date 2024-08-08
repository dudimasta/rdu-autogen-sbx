# program użwa user_proxy do rozmowy w języku naturalnym z asystentem. 
# po prostu uruchom i naciskaj emter aby się nie wcinać w rozmowę pomiędzy robotami
# powinien zostać wygenerowany plik rysujący graf w folderze ./coding
# po zakończeniu rozmowy robotów (gdy asystent napisze TERMINATE), to zadaj polecenie 
# narysowania innego grafu, np.:"please plot % change"

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
assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD.",
    #message="jadę na trzy dni w góry Gorce. Narysuj mapkę prezentującą szlaki, po których będę zwiedzał góry",
)