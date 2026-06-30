import logging

logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)


from langchain_chroma import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

CHROMA_PATH = Path(__file__).parent / "card_db"
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})


def retrieve_cards(query: str,k: int, issuer=None):
    if k<= 0 : 3
    if issuer:
        return vector_db.similarity_search(
            query,
            k=k,
            filter={"issuer": issuer}
        )

    return vector_db.similarity_search(
        query,
        k=k
    )