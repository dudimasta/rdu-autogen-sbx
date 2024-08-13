# program verifies if connection to Azure Aearch (Cognitive Search) is correct
# Program demonstruje użycie (Cognitive Search) do przeszukania zawartości indeksu (wektora)
# Program używa istniejącego wektora, nie buduje wektora.

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from typing import Dict, List, cast


service_endpoint = "https://lazarus-frc.search.windows.net"
index_name = "vector-1721723417068"
key = "x4c2CF3DoBDoiJibTJS9mSGt4OB3VcZlGE5HOKfem9AzSeCPVztv"

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

results = search_client.search(search_text="deprecated")
for result in results:
    print("    Completion: {}".format(result["chunk"]))

# answers = results.get_answers()
# for answer in answers:

#     print(answer)
# facets: Dict[str, List[str]] = cast(Dict[str, List[str]], results.get_facets())

#print("Catgory facet counts for hotels:")
#for facet in facets["category"]:
#    print("    {}".format(facet))

search_client.close();