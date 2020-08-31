# Imports:
from Property import Property

# A class defining a railway station
class Railway (Property):

    # The price of the railway if 2 railway stations are owned.
    price_2_owned = 0
    # The price of the railway if 3 railway stations are owned.
    price_3_owned = 0
    # The price of the railway if 4 railway stations are owned.
    price_4_owned = 0

    def __init__(self, property_id, purchase_price, rent, mortgage_value, price_2_owned = 0, price_3_owned = 0, price_4_owned = 0, property_name = "Unnamed Railway", property_type = 1, owner = ""):
        super().__init__(property_id, purchase_price, rent, mortgage_value, property_name=property_name, property_type = property_type, owner = owner)
        self.price_2_owned = price_2_owned
        self.price_3_owned = price_3_owned
        self.price_4_owned = price_4_owned
