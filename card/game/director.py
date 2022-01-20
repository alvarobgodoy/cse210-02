from game.card import Card


class Director:
    '''Someone who controls the game. 
    
    His responsability is to make decisions during the game.

    Attributes:
        score (int): How many points the player has.
        previous_card (int): The current card is displayed.
        next_card (int): The next card to be displayed after the user guess.
        user_guess (string): The decision of the user, higher or lower.
        is_playing (boolean): For the user to decide if the game continues or not.
    '''

    def __init__(self):
        '''Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        '''
        self.score = 300
        self.previous_card = 0
        self.next_card = 0
        self.user_guess = ''
        self.is_playing = True

    def start_game(self):
        '''Contains the main loop used to start the game.
        
        Args:
            self (Director): an instance of Director.
        '''
        while self.is_playing:
            self.initialize_round()
            self.do_outputs()
            self.keep_playing()

    def initialize_round(self):
        '''Initialize each round of the game.
        
        Args:
            self (Director): an instance of Director.
        '''
        if self.previous_card == 0:
            card = Card()
            self.previous_card = card.deal_card()
        else:
            self.previous_card = self.next_card
        print(f'\nThe card is : {self.previous_card}')
        self.user_guess = input('Higher or lower? [h/l] ')

    def do_outputs(self):
        '''Calculates the result of the round and assigns the points.
        
        Args:
            self (Director): an instance of Director.
        '''
        card = Card()
        self.next_card = card.deal_card()
        if self.user_guess == 'h' and self.previous_card < self.next_card:
            self.score += 100
        elif self.user_guess == 'l' and self.previous_card > self.next_card:
            self.score += 100
        else:
            self.score -= 75

        print(f'Next card was: {self.next_card}')
        print(f'Your score is: {self.score}')

    def keep_playing(self):
        '''Asks the user if they want to keep playing, if not the game ends.
        
        Args:
            self (Director): an instance of Director.
        '''
        play_again = input('Play again? [y/n] ')
        self.is_playing = (play_again == "y")
