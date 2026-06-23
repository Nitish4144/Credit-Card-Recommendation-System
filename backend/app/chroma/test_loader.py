from card_loader import load_card_documents

docs = load_card_documents()

print("Documents:", len(docs))

print("\nFirst Document:\n")
print(docs[0].page_content)