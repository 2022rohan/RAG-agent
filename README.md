# RAG Agent

A Retrieval-Augmented Generation (RAG) implementation built with LangChain, leveraging Google's Gemini models for embeddings and chat completions. This agent can retrieve context directly from web pages (via URLs) to accurately answer user queries based on the fetched data.

## Features

- **Web Document Loading:** Fetches content directly from a specified URL using standard web loader tools.
- **Document Splitting:** Chunks large web documents into smaller, manageable pieces to optimize similarity searching.
- **Google GenAI Embeddings:** Uses `gemini-embedding-001` for accurate and fast vector embeddings.
- **In-Memory/Local Vector Store:** Creates a vector representation of the document chunks for rapid context retrieval.
- **Tool-Calling Agent:** Employs a LangChain tool-calling agent wrapped around `gemini-2.5-flash-lite` to automatically execute the retrieval tool when it needs context to answer your prompts.

## Project Structure

```text
RAG Agent/
├── src/
│   ├── agent.py         # Defines and creates the RAG agent and injects retriever tools
│   ├── config.py        # Environment variables, model configuration, and LLM initialization
│   ├── embeddings.py    # Generates Google Gemini model embeddings  
│   ├── loader.py        # Logic to scrape and load documents from URLs
│   ├── retriever.py     # Contains the retrieval tool (factory) utilized by the agent
│   ├── splitter.py      # Implementation for splitting loaded documents into chunks
│   └── vector_store.py  # Logic to initialize and populate the vector store
├── main.py              # Main application entry point for running the RAG query pipeline
├── requirements.txt     # Python dependencies 
└── .env                 # (Must be created) Contains your API keys
```

## Prerequisites

- Python 3.8+
- [Google AI Studio API Key](https://aistudio.google.com/app/apikey)

## Setup

1. **Clone or navigate onto the project directory:**
   ```bash
   cd "RAG Agent"
   ```

2. **Install the project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Environment:**
   Create a `.env` file in the root directory (alongside `main.py`) with your Google API Key and your preferred user agent:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   USER_AGENT=RAG_Agent/1.0
   ```

## Usage

1. Open `main.py` and modify the `url` to point to the website you want to query information from.
2. Modify the `query` variable with the question you want to ask the agent.
3. Run the script:

```bash
python main.py
```

The agent will load the website, parse the context, create embeddings, define its retriever tool, and stream the final answer back to your console!
