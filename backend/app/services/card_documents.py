from langchain_core.documents import Document

def creat_documents(cards):

    docs = []

    for card in cards:

        text = f"""
        Card Name: {card.name}

        Annual Fee: {card.annual_fee}

        Cashback: {card.cashback_rate}

        Rewards: {card.reward_description}

        Perks: {card.perks}
        """


        docs.append(
            Document(
                page_content = text,metadata={
                    "card_name": card.name
                }
            )
        )
        return docs