# Imports:
import yaml
from ColouredProperty import ColouredProperty
from Railway import Railway
from Utility import Utility
from Card import Card
from random import randint

# A class defining a board
class Board:

    def __init__(self, players):
        self.player_positions = {}
        self.property_positions = []
        self.chance_positions = []
        self.community_chest_positions = []
        self.tax_positions = {}
        self.miscellaneous_positions = {}
        self.properties = []
        self.chance_cards = []
        self.community_chest_cards = []
        self.cards_drawn = {"Chance" : [], "Community Chest" : []}
        self.is_playing = False
        self.import_property_positions()
        self.import_chance_positions()
        self.import_community_chest_positions()
        self.import_tax_positions()
        self.import_miscellaneous_positions()
        self.import_properties()
        self.import_chance_cards()
        self.import_community_chest_cards()
        self.update(players)
        self.is_playing = True

    # Import the property positions from a yaml file      
    def import_property_positions(self):
        with open("positions.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                positions = temp["Positions"]
                properties = positions["Property"]
                # Import the coloured property positions:
                coloured = properties["Coloured"]
                for position in coloured:
                    self.property_positions.append(position)
                # Import the railway station positions:
                stations = properties["Stations"]
                for position in stations:
                    self.property_positions.append(position)
                # Import the utility property positions:
                utilities = properties["Utilities"]
                for position in utilities:
                    self.property_positions.append(position)
            except yaml.YAMLError as exc:
                print(exc)

    # Import the chance positions from a yaml file
    def import_chance_positions(self):
        with open("positions.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                positions = temp["Positions"]
                cards = positions["Cards"]
                chance = cards["Chance"]
                for position in chance:
                    self.chance_positions.append(position)
            except yaml.YAMLError as exc:
                print(exc)

    # Import the community chest positions from a yaml file
    def import_community_chest_positions(self):
        with open("positions.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                positions = temp["Positions"]
                cards = positions["Cards"]
                cc = cards["Community Chest"]
                for position in cc:
                    self.community_chest_positions.append(position)
            except yaml.YAMLError as exc:
                print(exc)
    # {position_number : {name: 'name', value: 'value'}, ...}
    # Import the tax positions from a yaml file
    def import_tax_positions(self):
        with open("positions.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                positions = temp["Positions"]
                tax = positions["Tax"]
                self.tax_positions = tax
            except yaml.YAMLError as exc:
                print(exc)

    # Import the miscellaneous positions from a yaml file
    def import_miscellaneous_positions(self):
        with open("positions.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                positions = temp["Positions"]
                misc = positions["Miscellaneous"]
                self.miscellaneous_positions = misc
            except yaml.YAMLError as exc:
                print(exc)

    # Import the properties from a yaml file
    def import_properties(self):
        with open("properties.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                properties = temp["Properties"]
                # Import the coloured properties:
                coloured = properties["Coloured"]
                for index in range(len(self.properties), len(coloured)):
                    prop = coloured[index]
                    name = prop["name"]
                    colour = prop["colour"]
                    purchase_price = prop["purchase_price"]
                    rent = prop["rent"]
                    price_with_1_house = prop["price_with_1_house"]
                    price_with_2_houses = prop["price_with_2_houses"]
                    price_with_3_houses = prop["price_with_3_houses"]
                    price_with_4_houses = prop["price_with_4_houses"]
                    price_with_hotel = prop["price_with_hotel"]
                    house_cost = prop["house_cost"]
                    mortgage_value = prop["mortgage_value"]
                    coloured_property = ColouredProperty(index, purchase_price, rent, price_with_1_house, price_with_2_houses, price_with_3_houses, price_with_4_houses, price_with_hotel, house_cost, mortgage_value, colour, property_name = name)
                    self.properties.append(coloured_property)
                # Import the railway stations:
                railways = properties["Stations"]
                for index in range(0, len(railways)):
                    prop = railways[index]
                    name = prop["name"]
                    purchase_price = prop["purchase_price"]
                    rent = prop["rent"]
                    price_2_owned = prop["price_2_owned"]
                    price_3_owned = prop["price_3_owned"]
                    price_4_owned = prop["price_4_owned"]
                    mortgage_value = prop["mortgage_value"]
                    railway = Railway(22 + index, purchase_price, rent, mortgage_value, price_2_owned, price_3_owned, price_4_owned, name)
                    self.properties.append(railway)
                # Import the utility properties:
                utilities = properties["Utilities"]
                for index in range(0, len(utilities)):
                    prop = utilities[index]
                    name = prop["name"]
                    purchase_price = prop["purchase_price"]
                    mortgage_value = prop["mortgage_value"]
                    utility = Utility(26 + index, purchase_price, mortgage_value, property_name = name)
                    self.properties.append(utility)
            except yaml.YAMLError as exc:
                print(exc)

    def import_chance_cards(self):
        with open("cards.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                cards = temp["Cards"]
                chance = cards["Chance"]
                for index in range(0, len(chance)):
                    card = chance[index]
                    name = card["name"]
                    action = card["action"]
                    must_use = card["must_use"]
                    card_object = Card(name, action, must_use)
                    self.chance_cards.append(card_object)
            except yaml.YAMLError as exc:
                print(exc)

    def import_community_chest_cards(self):
        with open("cards.yml", 'r') as stream:
            try:
                temp = yaml.safe_load(stream)
                cards = temp["Cards"]
                chance = cards["Community Chest"]
                for index in range(0, len(chance)):
                    card = chance[index]
                    name = card["name"]
                    action = card["action"]
                    must_use = card["must_use"]
                    card_object = Card(name, action, must_use)
                    self.community_chest_cards.append(card_object)
            except yaml.YAMLError as exc:
                print(exc)
    
    def update(self, players):
        for player in players:
            self.player_positions[player.player_id] = player.position
            player.cards["Chance"] = []
            player.cards["Community Chest"] = []

    def check_position(self, player):
        if player.position in self.property_positions:
            for prop in self.properties:
                if self.property_positions[prop.property_id] == player.position:
                    if prop.property_type == 0:
                        if prop.for_sale:
                            if player.should_purchase(prop):
                                player.purchase(prop)
                                prop.for_sale = False
                                prop.owner = player
                        else:
                            # TODO: Work out how many houses are on this property.
                            amount = prop.rent
                            player.pay(prop.owner, amount)
                    elif prop.property_type == 1:
                        if prop.for_sale:
                            if player.should_purchase(prop):
                                player.purchase(prop)
                                prop.for_sale = False
                                prop.owner = player
                        else:
                            # TODO: Work out how many stations are owned by this player
                            amount = prop.rent
                            player.pay(prop.owner, amount)
                    elif prop.property_type == 2:
                        if prop.for_sale:
                            if player.should_purchase(prop):
                                player.purchase(prop)
                                prop.for_sale = False
                                prop.owner = player
                        else:
                            # TODO: Work out how many utilities are owned by this player
                            amount = prop.rent
                            player.pay(prop.owner, amount)
                    else:
                        print("Error: Invalid property type")
        elif player.position in self.chance_positions:
            card = self.chance_cards[randint(0, len(self.chance_cards) - 1)]
            player.cards["Chance"].append(card)
            card.perform_action(player)
        elif player.position in self.community_chest_positions:
            pass
                        
    def get_property_position(self, property_id):
        return self.property_positions[property_id]        
