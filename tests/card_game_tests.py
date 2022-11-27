import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
      card1 = Card("Ace", 1)
      card2 = Card("Spades", 2)
    
      self.cardgame1 = CardGame(card1)
      self.cardgame2 = CardGame(card2)
      self.cards = (card1, card2)

    def test_can_check_for_ace(self):
        card1 = Card("Ace", 1)
        result = self.cardgame1.check_for_ace(card1)
        self.assertEqual(True, result)
    
    def test_can_check_not_ace(self):
        card2 = Card("Spades", 2)
        result = self.cardgame2.check_for_ace(card2)
        self.assertEqual(False, result)

    def test_if_returns_card2_as_highest_card(self):
        card1 = Card("Ace", 1)
        card2 = Card("Spades", 2)
        result = self.cardgame1.highest_card(card1, card2)
        self.assertEqual(card2, result)

    def test_if_returns_card1_as_highest_card(self):
        card1 = Card("Spades", 2)
        card2 = Card("Ace", 1)
        result = self.cardgame1.highest_card(card1, card2)
        self.assertEqual(card1, result)

    def test_can_get_cards_total_in_game(self):
        card1 = Card("Ace", 1)
        card2 = Card("Spades", 2)
        cards = (card1, card2)
        result = self.cardgame1.cards_total(cards)
        self.assertEqual("You have a total of 3", result)