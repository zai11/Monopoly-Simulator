# Imports:
from Property import Property

# A class defining a coloured property
class ColouredProperty (Property):

    # The colour of the property
    property_colour = ""
    # The price of the property with one house
    price_with_1_house = 0
    # The price of the property with two houses
    price_with_2_houses = 0
    # The price of the property with three houses
    price_with_3_houses = 0
    # The price of the property with four houses
    price_with_4_houses = 0
    # The price of the property with a hotel
    price_with_hotel = 0
    # The house cost of the property
    house_cost = 0

    def __init__(self, property_id, purchase_price, rent, price_with_1_house, price_with_2_houses, price_with_3_houses, price_with_4_houses, price_with_hotel, house_cost, mortgage_value, property_colour = "", property_type = 0, property_name = "Unnamed Property", for_sale = True, owner = ""):
        super().__init__(property_id, purchase_price, rent, mortgage_value, property_type = 0, property_name = property_name, owner = owner)
        self.property_colour = property_colour
        self.price_with_1_house = price_with_1_house
        self.price_with_2_houses = price_with_2_houses
        self.price_with_3_houses = price_with_3_houses
        self.price_with_4_houses = price_with_4_houses
        self.price_with_hotel = price_with_hotel
        self.house_cost = house_cost
