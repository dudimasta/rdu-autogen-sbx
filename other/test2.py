import os
from dotenv import load_dotenv

load_dotenv()

# Import Cognitive Search index ENV
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")
message=f"Search for 'What is the most recent release of D365 Finance?' in the {AZURE_SEARCH_INDEX} index"
print(message)