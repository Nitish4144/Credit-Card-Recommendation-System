from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from pathlib import Path

CHROMA_PATH = Path(__file__).parent / "card_db"
from card_loader import load_card_documents

documents = load_card_documents()

model = "all-MiniLM-L6-v2"
embeddings = HuggingFaceBgeEmbeddings( model_name=model)

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=str(CHROMA_PATH)  #path for the cards_vector_databse
)
print(f"Stored {len(documents)} cards")