# Program używa autogena:
# - agent user_proxy ma zarejestrowaną funkcję search(), 
#   która odpowiada za komuniację z wektorem i wyciągnięcie surowej zawartości 
#   po słowach kluczowych przekazanych w query
# - surowa zawartość (wyciągnięta z wektora) jest przekazywana do agenta COGSearch,
#   który dokonuje podsumowania i prezentuje co udało mu się zrozumieć z przekazanej zawartości
#   surowej wraz z referencją do pliku/plików źródłowych, na podstawie których został zbudowany indeks (wektor)
# https://microsoft.github.io/autogen/docs/notebooks/agentchat_azr_ai_search/
# https://microsoft.github.io/autogen/blog/2023/10/18/RetrieveChat/
import json
import os

import requests
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential

import autogen
from autogen import AssistantAgent, UserProxyAgent, register_function
from autogen.cache import Cache

# zmienne dot. konfuguracji AZ Search z pliku .env są ładowane do sesji
load_dotenv()

# Import Cognitive Search index ENV
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG = os.getenv("AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG")
AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")

credential = DefaultAzureCredential()
endpoint = AZURE_SEARCH_SERVICE_ENDPOINT

from azure.identity import AzureCliCredential

credential = AzureCliCredential()

client = SearchClient(AZURE_SEARCH_SERVICE_ENDPOINT, AZURE_SEARCH_INDEX, AzureKeyCredential(AZURE_SEARCH_KEY))

config_list= [{"model": os.getenv('autogen_model'), 
    "api_key": os.getenv('autogen_api_key'), 
    "base_url": os.getenv('autogen_base_url'),
    "api_type": os.getenv('autogen_api_type'),
    "api_version": os.getenv('autogen_api_version')}]

gpt4_config = {
    "cache_seed": 42,
    "temperature": 0.1,
    "config_list": config_list,
    "timeout": 120
}

def search(query: str):
    payload = json.dumps(
        {
            "search": query,
            # below is vector query: https://learn.microsoft.com/en-us/python/api/azure-search-documents/azure.search.documents.models.vectorquery?view=azure-python
            "vectorQueries": [{"kind": "text", "text": query, "k": 5, "fields": "vector"}],
            "queryType": "semantic",
            "semanticConfiguration": AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG,
            "captions": "extractive",
            "answers": "extractive|count-3",
            "queryLanguage": "en-US",
        }
    )

    response = list(client.search(payload))

    output = []
    __i = 20
    for result in response:
        __i = __i - 1
        if __i < 0:
            break
        result.pop("text_vector")
        output.append(result)
    return output

cog_search = AssistantAgent(
    name="COGSearch",
    system_message="You are a helpful AI assistant. "
    "You can help with Azure Cognitive Search."
    "Return 'TERMINATE' when the task is done.",
    llm_config=gpt4_config,
)

user_proxy = UserProxyAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

register_function(
    search,
    caller=cog_search,
    executor=user_proxy,
    name="search",
    description="A tool for searching the Cognitive Search index",
)

if __name__ == "__main__":
    import asyncio

    async def main():
        with Cache.disk() as cache:
            await user_proxy.a_initiate_chat(
                cog_search,
                # message="Search for 'What's new in D365 Finance release 40?' in the 'vector-1721723417068' index",
                #message="Search for 'What's new in most recent release of D365 Finance?' in the 'vector-1721723417068' index",
                message=f"Search for 'What is the most recent release of D365 Finance?' in the {AZURE_SEARCH_INDEX} index",
                # message="Search for 'What's new in D365 Finance?' in the 'vector-1721723417068' index",
                cache=cache,
            )

    #await main()
    asyncio.run(main())