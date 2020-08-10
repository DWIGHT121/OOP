# Wrestling Card Game
from random import shuffle
from enum import IntEnum

suits = ('HEART', 'SPADES', 'DIAMONDS', 'CLUBS')
values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


class CardRank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


RANKS = {
    '2': CardRank.TWO,
    '3': CardRank.THREE,
    '4': CardRank.FOUR,
    '5': CardRank.FIVE,
    '6': CardRank.SIX,
    '7': CardRank.SEVEN,
    '8': CardRank.EIGHT,
    '9': CardRank.NINE,
    '10': CardRank.TEN,
    'J': CardRank.JACK,
    'Q': CardRank.QUEEN,
    'K': CardRank.KING,
    'A': CardRank.ACE
}


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.rank = RANKS[value]

    def __str__(self):
        return self.value + self.suit


class ShuffledDeck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

        shuffle(self.deck)

    def draw(self):
        return self.deck.pop()


deck = ShuffledDeck()
for i in range(0, 52):
    card1 = deck.draw()
    print(card1)
