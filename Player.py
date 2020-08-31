
# A class defining a Player.
class Player:

    def __init__(self, player_id, strategy, cash = 1500, position = 0, prop_landed_counter = 0):
        self.player_id = player_id
        self.strategy = strategy
        self.cash = cash
        self.position = position
        self.properties = []
        self.cards = {"Chance" : [], "Community Chest" : [], "Other" : []}
        self.prop_landed_counter = prop_landed_counter
        self.utility_num = 0
        self.station_num = 0
        self.brown_num = 0
        self.light_blue_num = 0
        self.pink_num = 0
        self.orange_num = 0
        self.red_num = 0
        self.yellow_num = 0
        self.green_num = 0
        self.dark_blue = 0

    # Return whether or not the player can purchase the given property.
    # That is, the property is for sale and the player has more cash than
    # the property's purchase price.
    def can_purchase(self, prop):
        if prop.for_sale and self.cash >= prop.purchase_price:
            return True
        return False

    # Return whether or not the player should purchase the given property
    # based on the player's strategy value.
    def should_purchase(self, prop):
        if self.strategy == 0:
            return False
        elif self.strategy == 1:
            if self.can_purchase(prop):
                return True
            return False
        elif self.strategy == 2:
            if self.can_purchase(prop) and prop.purchase_price >= 220:
                return True
            return False
        elif self.strategy == 3:
            if self.can_purchase(prop) and prop.purchase_price <= 200:
                return True
            return False
        elif self.strategy == 4:
            if self.can_purchase(prop) and self.prop_landed_counter % 2 == 0:
                return True
            return False
        elif self.strategy == 5:
            if self.can_purchase(prop) and self.prop_landed_counter % 3 == 0:
                return True
            return False
        else:
            print("ERROR: Invalid strategy for player ", self.player_id + ":", self.strategy)

    def purchase(self, prop):
        if self.should_purchase(prop):
            self.cash -= prop.purchase_price
            self.properties.append(prop)
            
    def pay(self, player, amount):
        self.cash -= amount
        player.cash += amount
