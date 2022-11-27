import unittest
from src.card import Card
from src.card_game import CardGame

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card("Ace", 1)

    def test_card_has_suit(self):
        self.assertEqual("Ace", self.card.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.card.value)