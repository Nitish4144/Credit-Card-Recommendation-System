from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
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

# def retrieve_cards(query: str):
#     return retriever.invoke(query)


def retrieve_cards(query: str, issuer=None):

    if issuer:
        return vector_db.similarity_search(
            query,
            k=3,
            filter={"issuer": issuer}
        )

    return vector_db.similarity_search(
        query,
        k=3
    )