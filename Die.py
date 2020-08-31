from random import randint

# A class defining a six-sided die
class Die:

    value = 0

    def roll(self):
        self.value = randint(1,6)
        return self.value

    
