import bs4
from langchain_community.document_loaders import WebBaseLoader

def web_load_docs(url):
    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs={"parse_only": bs4_strainer},
    )
    docs = loader.load()
    return docs
