from game import Card, ManageDeck, EvaluateHand


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
        count_of_removed_cards = hand.discard_cards(which_cards)
        # Deal two new cards and remove them from the existing deck
        new_cards = deck.deal_cards(count_of_removed_cards)
        # card the new cards to the players hand
        hand.add_cards(new_cards)
        print(f"player cards are now: {hand.cards}")
        # evaluate the player hand
        evaluator = EvaluateHand(hand)
        print(evaluator.check_one_pair())

    else:
        # evaluate cards
        pass

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
