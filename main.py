from src.loader import web_load_docs
from src.splitter import split_docs
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store, store_docs
from src.agent import build_agent
import os
from dotenv import load_dotenv

load_dotenv()

url="any_url_you_think_has_some_information"

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

docs=web_load_docs(url)

docs_split=split_docs(docs)

vector_store=store_docs(docs_split)

agent=build_agent(vector_store)

query = (
    "what is tool integration done in AI agents?"
)

for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    event["messages"][-1].pretty_print()



