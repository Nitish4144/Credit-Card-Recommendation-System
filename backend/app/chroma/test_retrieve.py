from retriever import retrieve_cards

docs = retrieve_cards(
    "Best journey card with lounge access"
)

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.metadata)
    print(doc.page_content)