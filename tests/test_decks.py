import unittest
from app.decks import Deck


class CardsTest(unittest.TestCase):

    def testInit(self):
        deck = Deck()
        self.assertEqual(deck.suits, ['hearts', 'clubs', 'diamonds', 'spades'])
        self.assertEqual(deck.values, [x for x in xrange(13)])
        self.assertEqual(len(deck.cards), 52)

    def testDeal(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        card = deck.deal()
        self.assertEqual(len(deck.cards), 51)
        self.assertIn(card.suit, ['hearts', 'clubs', 'diamonds', 'spades'])
        self.assertTrue(0 <= card.value <= 12)

    # Flaky, but quick. Assert first card is not equal to first card after shuffle.
    def testShuffle(self):
        deck = Deck()
        top_card = deck.cards[0]
        deck.shuffle()
        shuffled_card = deck.cards[0]
        self.assertTrue(top_card.value != shuffled_card.value or top_card.suit != shuffled_card.suit)

    # Flaky, but quick. Assert first card is not equal to first card after shuffle.
    def testShuffleBuiltIn(self):
        deck = Deck()
        top_card = deck.cards[0]
        deck.shuffle_built_in()
        shuffled_card = deck.cards[0]
        self.assertTrue(top_card.value != shuffled_card.value or top_card.suit != shuffled_card.suit)
