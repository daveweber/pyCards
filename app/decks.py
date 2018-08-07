# -*- coding: utf-8 -*-

from random import randint, shuffle
from cards import Card

class Deck(object):

    def __init__(self, suits=None, values=None):
        self.suits = suits if suits is not None else ['hearts', 'clubs', 'diamonds', 'spades']
        self.values = values if values is not None else [x for x in xrange(13)]
        self.cards = [Card(suit,value) for suit in self.suits for value in self.values]

    # Implements the Fisher-Yates algorithm: https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    def shuffle (self):
        deck_size = xrange(len(self.cards))
        for i in deck_size:
            j = randint(deck_size[0], deck_size[-1])
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        
        return self.cards

    # Uses built in shuffle method from random library: https://docs.python.org/2/library/random.html
    def shuffle_built_in (self):
        shuffle(self.cards)
        return self.cards

    def deal (self):
        return self.cards.pop()