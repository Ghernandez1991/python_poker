from game import Card, ManageDeck


def main():
    # init a deck of cards
    deck = ManageDeck(1)

    # draw an init hand of cards
    hand = deck.generate_first_hand()
    for index, card in enumerate(hand.cards):
        print(f"card number {index +1 }: {card}")

    discard = input("Enter y or n if you wish to discard any cards in your hand\n")
    if discard in ["y", "Y", "yes", "Yes"]:
        # which cards do you want to get rid of
        which_cards = input(
            "enter the card numbers you want to get rid of, seperated by a comma(1,2)\n"
        )
        # remove those cards from the hand
        hand.discard_cards(which_cards)
        # insert two new cards
    else:
        # evaluate cards
        pass

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
