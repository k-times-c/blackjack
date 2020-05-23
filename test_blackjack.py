"""test_blackjack.py -- test suite for blackjack.py"""

import unittest
from blackjack import Card, Deck, Player, Round, Dealer

class TestCard(unittest.TestCase):
    """test the card"""
    def setUp(self):
        """set up instance of card to test functionality"""
        self.card = Card('Ace', 'Spades', 1)

    def tearDown(self):
        pass

    def test_get_name(self):
        """test getter function"""
        self.assertEqual(self.card.name, 'Ace')

    def test_set_name(self):
        """test setter function"""
        self.card.set_name('King')
        self.assertEqual(self.card.name, 'King')

    def test_get_suit(self):
        """test getter function"""
        self.assertEqual(self.card.suit, 'Spades')

    def test_set_suit(self):
        """test setter function"""
        self.card.set_suit('Hearts')
        self.assertEqual(self.card.suit, 'Hearts')

    def test_get_value(self):
        """test getter function"""
        self.assertEqual(self.card.value, 1)

    def test_set_value(self):
        """test setter function"""
        self.card.set_value(2)
        self.assertEqual(self.card.value, 2)


class TestDeck(unittest.TestCase):
    """test deck class"""
    def setUp(self):
        """set up to test deck"""
        self.test_deck = Deck()

    def test___len__(self):
        self.assertEqual(len(self.test_deck), 52)

    def test_shuffle(self):
        self.assertEqual(self.test_deck.shuffle(), None)

    def test_take_top_card(self):
        self.assertIsInstance(self.test_deck.take_top_card(), Card)

class TestPlayer(unittest.TestCase):
    """test the instance of player"""
    def setUp(self):
        self.player = Player('player1')
        self.card = Card('Ace', 'Diamonds', 1)

    def test_add_card_to_hand(self):
        """test whether you add a hand"""
        self.player.add_card_to_hand(self.card)
        self.assertEqual(self.player.hand[0], self.card)

    def test_set_hand(self):
        """test set hand method"""
        with self.assertRaises(ValueError):
            self.player.set_hand(1)
            self.player.set_hand(tuple(1))
            self.player.set_hand(bool)

    def test_check_if_busted(self):
        """tests if busted works correctly"""
        self.assertFalse(self.player.check_if_busted())
        self.player.set_score(21)
        self.assertFalse(self.player.check_if_busted())
        self.player.set_score(22)
        self.assertTrue(self.player.check_if_busted())

    def test_set_is_in_game(self):
        """test setter method for the is_in_game attribute"""
        with self.assertRaises(ValueError):
            self.player.set_is_in_game(list)
            self.player.set_is_in_game('string')
            self.player.set_is_in_game(bool)

        result = self.player.set_is_in_game(True)
        self.assertEqual(result, True)

    def test_update_score(self):
        """test update_score method"""
        card1 = Card("Ace", "Hearts", 1)
        card2 = Card("Ace", "Hearts", 1)
        card3 = Card("Ace", "Hearts", 1)

        self.player.set_hand([card1, card2, card3])
        self.assertEqual(self.player.update_score(), 3)

class TestRound(unittest.TestCase):
    """test round class"""
    def setUp(self):
        self.round = Round()

    def test___init___(self):
        """test init function"""
        self.assertIsInstance(self.round.deck, Deck)
        self.assertIsInstance(self.round.dealer, Dealer)

    def test_deal_cards(self):
        """make sure each step is working appropriately"""
        # 1. shuffle deck
        self.assertNotEqual(self.round.deck, Deck().deck)
        # TODO: finish test case

    def test_hit_players(self):
        """test for players"""
        # TODO: finish test case
        pass
