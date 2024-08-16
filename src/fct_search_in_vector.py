def search_in_vector(query: str):
    import json
    from azure.search.documents import SearchClient
    import os
    from azure.identity import DefaultAzureCredential
    from azure.core.credentials import AzureKeyCredential
    from azure.identity import AzureCliCredential
    from dotenv import load_dotenv

    # zmienne dot. konfuguracji AZ Search z pliku .env są ładowane do sesji
    load_dotenv()

    AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")
    AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
    AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG = os.getenv("AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG")
    AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    endpoint = AZURE_SEARCH_SERVICE_ENDPOINT

    client = SearchClient(AZURE_SEARCH_SERVICE_ENDPOINT, AZURE_SEARCH_INDEX, AzureKeyCredential(AZURE_SEARCH_KEY))
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