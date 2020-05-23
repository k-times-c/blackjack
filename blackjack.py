'''blackjack.py -- play the classic casino game'''

import random

class Card:
    """instance card"""
    def __init__(self, name, suit, value=0):
        self.name = name
        self.suit = suit
        self.value = value

    def set_name(self, name):
        """set the name of the card"""
        self.name = name

    def get_name(self):
        """get the name of the card"""
        return self.name

    def set_value(self, value):
        """set the value of the card"""
        self.value = value

    def get_value(self):
        """get the value of the card"""
        return self.value

    def set_suit(self, suit):
        """set the suit of the card"""
        self.suit = suit

    def get_suit(self):
        """get the suit of the card"""
        return self.suit

    def __repr__(self):
        """print out card's name and suit"""
        return f'{self.name} of {self.suit}'

class Deck:
    """creating instance of deck to play game"""

    def __init__(self):
        self.num_of_cards = 52

        number_cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        face_cards   = [ 'Jack', 'Queen', 'King']
        card_suits   = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

        self.deck = []
        for suit in card_suits:
            for rank, name in enumerate(number_cards, start=1):
                self.deck.append(Card(name, suit, rank))

        rank = 10
        for suit in card_suits:
            for name in face_cards:
                self.deck.append(Card(name, suit, rank))

        self.is_shuffled = False

    def __repr__(self):
        """returns all cards within the deck via a string output"""
        deck_string = 'DECK \n__________'
        for card in self.deck:
            deck_string += f'\n{card}'

        deck_string += '\n_________'

        return deck_string

    def __len__(self):
        """count the deck of cards"""
        return len(self.deck)

    def get_num_of_cards(self):
        """get the number of cards that haven't been dealt"""
        return self.num_of_cards

    def shuffle(self):
        """shuffle the deck"""
        random.shuffle(self.deck)
        self.set_is_shuffled(True)

    def take_top_card(self):
        """returns the top card from the stack"""
        card = self.deck.pop(0)
        self.num_of_cards -= 1
        return card

    def get_is_shuffled(self):
        """getter for shuffled method"""
        result = self.is_shuffled
        return result

    def set_is_shuffled(self, condition):
        """setter method for is_shuffled"""
        if not isinstance(condition, bool):
            raise ValueError
        self.is_shuffled = condition

class Player:
    """instance of player has attribute hand, and can play"""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.is_not_staying_at_score = True
        self.is_in_game = True

    def __repr__(self):
        """repr method for player: returns his/her cards and score"""
        res = f"""
                ----------\n
                {self.name}\n
                cards in hand: {self.hand}\n 
                score: {self.score}\n
                ----------"""
        return res

    def get_name(self):
        """getter method for name attribute"""
        return self.name

    def set_name(self, name):
        """setter method for name attribute"""
        self.name = name

    def get_hand(self):
        """get all cards with array self.hand"""
        return self.hand

    def set_hand(self, hand):
        """sets the input list or tuple to self.hand"""
        if not isinstance(hand, (list, tuple)):
            raise ValueError
        if any(not isinstance(element, Card) for element in hand):
            raise ValueError
        self.hand = hand

    def get_score(self):
        """get score"""
        score = self.score
        return int(score)

    def set_score(self, score):
        """get point total for a given player's hand"""
        self.score = score
        return self.score

    def get_is_not_staying_at_score(self):
        """getter for bool"""
        return self.is_not_staying_at_score

    def set_is_not_staying_at_score(self, condition):
        """setter for bool"""
        if not isinstance(condition, bool):
            raise ValueError
        self.is_not_staying_at_score = condition
        return self.get_is_not_staying_at_score()

    def get_is_in_game(self):
        """get whether they are still in the game"""
        return self.is_in_game

    def set_is_in_game(self, condition):
        """setter method for is_in_game"""
        if not isinstance(condition, bool):
            raise ValueError
        self.is_in_game = condition

        return self.get_is_in_game()

    def update_score(self):
        """resets and update score"""
        self.score = 0
        for card in self.hand:
            self.score += card.get_value()
        return self.get_score()

    def add_card_to_hand(self, card):
        """add card to hand"""
        if not isinstance(card, Card):
            raise ValueError
        self.hand.append(card)

    def check_if_busted(self):
        """changes player to inactive when the player busts"""
        if self.get_score() > 21:
            print(self.get_hand())
            print(f'{self.name} HAS BUSTED!\n\n')
            print(f'______________________________')
            self.set_is_in_game(False)
            return True
        return False

class Dealer(Player):
    """instance of the dealer"""
    def __init__(self):
        super().__init__('Dealer')


class Round:
    """instance of a round of black_jack"""
    def __init__(self, players=1):
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = [Player(f'player{index}') for index in range(1, players+1)]

    def _deal_card_to_player(self, player):
        dealt_card = self.deck.take_top_card()
        player.add_card_to_hand(dealt_card)
        player.update_score()

    def deal_cards(self):
        """
        gives one card to the dealer, and then gives a hand of two cards to
        other players, and shows players hands
        """
        # 1. shuffle deck
        self.deck.shuffle()

        # 2. deal two cards to every player
        for _ in range(2):
            for player in self.players:
                # deal card to each player
                self._deal_card_to_player(player)

            # then the dealer gets one card
        self._deal_card_to_player(self.dealer)

    def _hit_for(self, player):
        """hit for individual player"""
        if not isinstance(player, Player):
            raise ValueError

        response = ''
        while player.get_is_not_staying_at_score() and player.get_is_in_game():
            print(player)
            response = input(f'{player.name} would you like another card? (input y or n) ')
            if response not in ['y', 'n']:
                print('please print y or n')
                continue
            if response == 'y':
                self._deal_card_to_player(player)
                player.update_score()
                player.check_if_busted()
                continue
            # if they answer no, we set their staying score to false
            player.set_is_not_staying_at_score(False)

    def hit_players(self):
        """let each player hit"""
        if not self.deck.get_is_shuffled():
            self.deck.shuffle()
        for player in self.players:
            self._hit_for(player)

    def determine_winning_score_and_players(self):
        """return a named_tuple of the highest score, and those who won"""
        winning_score = -1
        players_who_have_not_busted = [player
                                       for player in self.players
                                       if player.is_in_game is True
                                      ]
        players_with_winning_score = []
        for player in players_who_have_not_busted:
            if player.get_score() > winning_score:
                winning_score = player.get_score()
        for player in self.players:
            if player.get_score() == winning_score:
                players_with_winning_score.append(player)
        return (winning_score, players_with_winning_score)

    def dealers_turn(self, winners):
        """dealer goes"""
        if not isinstance(winners, list):
            raise ValueError

        if all(not isinstance(player, Player) for player in winners):
            raise ValueError

        self._deal_card_to_player(self.dealer)
        self._hit_for(self.dealer)
        # pull winner score
        winning_score = winners[0].get_score()
        # pull dealer's score
        dealer_score = self.dealer.get_score()
        # compare dealer to players
        if dealer_score < winning_score or dealer_score > 21:
            winners_string = ''
            for player in winners:
                winners_string += player.name
            print(f'{winners_string} win(s)!')
        elif dealer_score > winning_score:
            print('The house wins')
        else: # it's a tie
            print("it's a tie")
def main():
    """main testing logic"""
    players = input("how many players are at the table ")
    black_jack = Round(int(players))
    black_jack.deal_cards()
    print(black_jack.players)
    print('====================')
    print('THE HOUSE')
    print(black_jack.dealer)
    print('====================')
    print('====================')
    print('PLAYER TURNS')
    black_jack.hit_players()
    winning_total, winning_players = black_jack.determine_winning_score_and_players()
    print(f'the highest score is {winning_total}')
    black_jack.dealers_turn(winning_players)

if __name__ == '__main__':
    main()
