from game import Card, ManageDeck


def main():
    # init a deck of cards
    deck = ManageDeck(1)

    # draw an init hand of cards
    hand = deck.generate_first_hand()
    for index, card in enumerate(hand.cards):
        print(f"card number {index +1 }: {card}")

    discard = input("Enter y or n if you wish to discard any cards in your hand\n")

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
