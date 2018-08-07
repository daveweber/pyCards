import unittest
from app.cards import Card


class CardsTest(unittest.TestCase):

    def testInit(self):
        card = Card('spades', 3)
        self.assertEqual(card.suit, 'spades')
        self.assertEqual(card.value, 3)
