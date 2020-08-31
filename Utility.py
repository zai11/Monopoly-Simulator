# Imports:
from Property import Property

# A class defining a utility property
class Utility (Property):
    
    def __init__(self, property_id, purchase_price, mortgage_value, rent = -1, property_type = 2, property_name = "Unnamed Utility", owner = ""):
        super().__init__(property_id, purchase_price, mortgage_value, rent, property_type = property_type, property_name = property_name, owner = owner)
