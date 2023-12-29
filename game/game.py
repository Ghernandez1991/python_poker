from dataclasses import dataclass
import random
from typing import List
from collections import defaultdict


@dataclass
class Card:
    """
    Card class used to create instances of Cards. These objects are used in the Hand and ManageDeck class
    and are the base class in the game.
    Value, Color and Suit are based on the default values of a 52 card deck.
    """

    value: str
    color: str
    suit: str


@dataclass
class Hand:
    """
    Hand class used to create a players hard of cards. A hand contains 5 card objects. A Hand instance is created
    by the manage deck class. Uses will use this class to discard cards from their hand, or add cards.
    """

    cards: list = None

    def __post_init__(self):
        if self.cards is None:
            self.cards = []

    def add_cards(self, cards):
        """When a hand is first generated, it is initialized with no cards.
        The ManageDeck class then passes random cards to the Hand instance while removing them from the deck
        """

        self.cards.extend(cards)

    def discard_cards(self, discarded_cards: str) -> int:
        discarded_cards = discarded_cards.split(",")
        index_to_remove = [int(card) - 1 for card in discarded_cards]
        print(index_to_remove)
        self.cards = [
            card
            for index, card in enumerate(self.cards)
            if index not in index_to_remove
        ]
        print(self.cards)

        return len(discarded_cards)


@dataclass
class ManageDeck:
    number_of_decks: int

    def __post_init__(self):
        self.colors = ["Black", "Red"]
        self.suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.values = {
            "Ace",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
        }
        self.required_cards = self.number_of_decks * 52
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        for suit in self.suits:
            for value in self.values:
                color = "Black" if suit in ("Spades", "Clubs") else "Red"
                self.cards.append(Card(value=value, color=color, suit=suit))

    def generate_first_hand(self) -> Hand:
        # select 5 cards at random from the deck to give to the user, and to remove those cards from use
        cards_to_remove = random.sample(self.cards, k=5)
        print("we are removing the following cards")
        print(cards_to_remove)
        indexes_to_remove = []

        for outter_card in cards_to_remove:
            print(
                f"outter card is {outter_card.value} of {outter_card.suit} ({outter_card.color})"
            )
            for index, inner_card in enumerate(self.cards):
                print(
                    f"inner card is {inner_card.value} of {inner_card.suit} ({inner_card.color})"
                )
                if (
                    inner_card.value == outter_card.value
                    and inner_card.color == outter_card.color
                    and inner_card.suit == outter_card.suit
                ):
                    print("found a match")
                    indexes_to_remove.append(index)
                else:
                    continue
        print(indexes_to_remove)
        self.cards = [
            elem
            for index, elem in enumerate(self.cards)
            if index not in indexes_to_remove
        ]

        print(f"the deck now has {len(self.cards)} cards left")
        for card in self.cards:
            print(f"{card.value} of {card.suit} ({card.color})")

        print(f"cards going to the player are {cards_to_remove}")
        player_hand = Hand()

        player_hand.add_cards(cards_to_remove)

        return player_hand

    def deal_cards(self, number_of_cards: int):
        # get a random sample of cards from the exiting cards in the deck
        cards_to_remove = random.sample(self.cards, k=number_of_cards)
        print("we are removing the following cards from the deck and giving to player")
        print(cards_to_remove)
        indexes_to_remove = []
        # remove those cards from the deck
        for outter_card in cards_to_remove:
            print(
                f"outter card is {outter_card.value} of {outter_card.suit} ({outter_card.color})"
            )
            for index, inner_card in enumerate(self.cards):
                print(
                    f"inner card is {inner_card.value} of {inner_card.suit} ({inner_card.color})"
                )
                if (
                    inner_card.value == outter_card.value
                    and inner_card.color == outter_card.color
                    and inner_card.suit == outter_card.suit
                ):
                    print("found a match")
                    indexes_to_remove.append(index)
                else:
                    continue
        print(indexes_to_remove)
        # use list comprehension to only get cards that are not in the indexes we are removing
        self.cards = [
            elem
            for index, elem in enumerate(self.cards)
            if index not in indexes_to_remove
        ]

        print(f"the deck now has {len(self.cards)} cards left")
        for card in self.cards:
            print(f"{card.value} of {card.suit} ({card.color})")

        print(f"cards going to the player are {cards_to_remove}")

        return cards_to_remove


class EvaluateHand:
    def __init__(self, hand) -> None:
        self.hand = hand

    def check_one_pair(self):
        value_counts = defaultdict(int)
        for card in self.hand.cards:
            value_counts[card.value] += 1

        # Check for a pair
        for value, count in value_counts.items():
            if count == 2:
                return f"Pair of {value}s found"

        return "No pair found"
