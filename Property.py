# A class defining a property
class Property:
    # The id the property has
    property_id = 0
    # The type of property it is:
    # 0 - coloured
    # 1 - station
    # 2 - utility
    property_type = 0
    # The name of the property
    property_name = ""
    # The purchase price of the property
    purchase_price = 0
    # The rent of the property
    rent = 0
    # The mortgage value of the property
    mortgage_value = 0
    # Whether or not the property is for sale
    for_sale = True

    owner = ""
    

    def __init__(self, property_id, purchase_price, rent, mortgage_value, property_type = -1, property_name = "Unnamed Property", for_sale = True, owner = ""):
        self.property_id = property_id
        self.property_type = property_type
        self.property_name = property_name
        self.purchase_price = purchase_price
        self.rent = rent
        self.mortgage_value = mortgage_value
        self.for_sale = for_sale
        self.owner = owner
