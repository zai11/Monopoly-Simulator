# A class defining a card
class Card:

    def __init__(self, name = "Unnamed Card", action = "Unspecified Action", must_use = True):
        self.name = name
        self.action = action
        self.must_use = must_use

    def perform_action(self, player):
        # TODO: write this method
        pass

    
