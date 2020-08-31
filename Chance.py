# Imports:
import yaml
from Card import Card
from random import randint

# A class defining the chance card pile
class Chance:
    
    cards = []

    def __init__(self):
        self.import_cards()

    # Import the chance cards from a yaml file
    def import_cards(self):
        with open("cards.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                root = temp["Cards"]
                cards = root["Chance"]
                for index in range(0, 15):
                    card = cards[index]
                    name = card["name"]
                    action = card["action"]
                    must_use = card["must_use"]
                    card_object = Card(name, action, must_use)
                    self.cards.append(card_object)
            except yaml.YAMLError as exc:
                print(exc)

    # Draw a card
    def draw(self):
        number = randint(0, len(self.cards))
        return self.cards[number]
