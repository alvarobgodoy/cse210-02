import random

class Card:

    def __init__(self):
        self.value = 0

    def deal_card(self):
        self.value = random.randint(1, 13)
        return self.value