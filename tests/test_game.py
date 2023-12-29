# test_game.py

import pytest
from game.game import Card, Hand, ManageDeck, EvaluateHand


# Test Card class
def test_card_instantiation():
    # Your instantiation tests for Card class here
    card = Card("Five", "Red", "Diamonds")
    assert card.value == "Five"
    assert card.color == "Red"
    assert card.suit == "Diamonds"


# Test Hand class
def test_hand_initialization():
    # Test initialization of an empty hand
    hand = Hand()
    assert len(hand.cards) == 0

    # Add test cases for adding cards and discarding cards
    # ...


# Test ManageDeck class
def test_deck_generation():
    # Test generation of the deck and validate the number of cards
    # ...
    pass


def test_generate_initial_hand():
    # Test generating the initial hand and validate the hand's content and the remaining deck
    # ...

    deck = ManageDeck(1)

    # draw an init hand of cards
    hand = deck.generate_first_hand()
    assert len(hand.cards) == 5


def test_deal_cards():
    # Test dealing cards and check if the deck and dealt cards are updated correctly
    # ...
    pass


# Test EvaluateHand class
def test_check_one_pair():
    # Test the check_one_pair method for different scenarios
    # ...
    pass
