import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
USER_AGENT = os.getenv("USER_AGENT")

EMBEDDING_MODEL = "models/gemini-embedding-001"

LLM_MODEL = "models/gemini-1.5-flash"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

model = init_chat_model("google_genai:gemini-2.5-flash-lite")
