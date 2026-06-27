from app.chroma.retriever import retrieve_cards


def build_card_context(card_names):

    context = ""

    for card_name in card_names:

        docs = retrieve_cards(
            query=card_name,
            k=1
        )

        if docs:
            context += docs[0].page_content
            context += "\n\n"

    return context