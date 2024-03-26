#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Card:
    suit_order ={"A":14, "K":13, "Q":12, "J":11}

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        for i in range(2,11):
            Card.suit_order[str(i)] = i
        

    def __eq__(self, other: object) -> bool:
        return self.rank ==other.rank
    def __gt__(self,other:object) -> bool:
        return Card.suit_order[self.rank] > Card.suit_order[other.rank]


class Deck:
    suits = 'H D S C'.split()
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self) -> None:
        self.deck = []
        self.create_deck()
        shuffle(self.deck)
    
    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit,rank))
    def distribute_cards(self, hand1,hand2):
        while len(self.deck) >0:
            hand1.add_card(self.deck.pop())
            hand2.add_card(self.deck.pop())

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self) -> None:
        self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)
    def remove_card(self):
        return self.hand.pop()
    def add_card_to_bottom(self,card):
        if isinstance(card,list):
            for c in card:
                self.add_card_to_bottom(c)
        else:
            self.hand.insert(0,card)
    def is_empty(self):
        return len(self.hand)==0
    def __len__(self):
        return len(self.hand)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand
    
    def show_cards(self, num):
        cards = []
        if len(self.hand) < num:
            while not self.hand.is_empty():
                cards.append(self.hand.remove_card())
            return cards
        for i in range(num):
            cards.append(self.hand.remove_card())
        return cards


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
hand1 = Hand()
hand2 = Hand()
deck = Deck()
deck.distribute_cards(hand1,hand2)
player1 = Player("Joe", hand1)
player2 = Player("Ali", hand2)
# Use the 3 classes along with some logic to play a game of war!
running = True

while running:
    card1 = player1.show_cards(1)[0]
    card2 = player2.show_cards(1)[0]
    if card1>card2:
        player1.hand.add_card_to_bottom(card1)
        player1.hand.add_card_to_bottom(card2)
    elif card2>card1:
        player2.hand.add_card_to_bottom(card1)
        player2.hand.add_card_to_bottom(card2)
    else:
        cards1 = player1.show_cards(3)
        cards2 = player1.show_cards(3)
        if cards1[-1]>cards2[-1]:
            player1.hand.add_card_to_bottom(cards1+cards2)

        elif card2>card1:
            player2.hand.add_card_to_bottom(cards1+cards2)

    if player1.hand.is_empty():
        print(f"{player2.name} Won!")
        running = False
    elif player2.hand.is_empty():
        print(f"{player1.name} Won!")
        running = False