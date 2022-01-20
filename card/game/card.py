import random

class Card:
    '''Someone who controls the game. 
    
    His responsability is to make decisions during the game.

    Attributes:
        value (int): The value of the card (from 1 to 13).
    '''

    def __init__(self):
        '''Constructs a new Card.
        
        Args:
            self (Card): an instance of Card.
        '''
        self.value = 0

    def deal_card(self):
        '''Deals the card and return a random one from 1 to 13
        
        Args:
            self (Card): an instance of Card.
        '''
        self.value = random.randint(1, 13)
        return self.value