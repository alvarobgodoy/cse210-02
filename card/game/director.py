from game.card import Card


class Director:
    '''
    '''

    def __init__(self):
        '''
        Player starts with 300 points
        current points
        total points
        '''
        self.current_points = 0
        self.total_points = 0
        self.random_card = 0
        self.next_card = 0
        self.user_guess = ''
        self.is_playing = True

    def start_game(self):
        