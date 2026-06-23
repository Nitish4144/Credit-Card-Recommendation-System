from app.chroma.retriever import retrieve_cards

def build_card_context(card_names):

    context= ""

    for card_name in card_names:

        docs = retrieve_cards(card_name)

        if docs:
            context += docs[0].page_content
            context += "\n\n"

    return context