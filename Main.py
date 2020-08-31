# Imports:
from Chance import Chance
from CommunityChest import CommunityChest
from Player import Player
from Board import Board
from Die import Die
import yaml


# Setup game round storage:
game_rounds = {'Monopoly Game': {}}

# Setup cards:
chance = Chance()
community_chest = CommunityChest()

# Setup players:
players = []
for i in range(0, 6):
    player = Player(i, i)
    players.append(player)

# Setup board:
board = Board(players)

# Setup dice:
dice = [Die(), Die()]

# Game Loop:
#while board.is_playing():
def gameLoop():
    for player in players:
        to_move = 0
        for die in dice:
            to_move += die.roll()
        player.position += to_move
        board.check_position(player)
    add_round()
    board.update(players)

def display():
    print("---        Round:        ---\n")
    print("Positions:")
    for player in players:
        print(player.position)
    print("Balances:")
    for player in players:
        print(player.cash)
    print("Properties:")
    for player in players:
        if len(player.properties) > 0:
            print(str(player.player_id) + ") ", end='')
            for prop in player.properties:
                print(prop.property_name, end='')
            print('')
    print("Cards Drawn:")
    for player in players:
        if len(player.cards) > 0:
            print(str(player.player_id) + ":")
            print("Chance:")
            chance = player.cards["Chance"]
            for card in chance:
                print(card.name + " ", end='')
            print("Community Chest:")
            cc = player.cards["Community Chest"]
            for card in cc:
                print(card.name + " ", end='')
            
    print("\n\n")

def add_round():
    root = game_rounds["Monopoly Game"]
    positions = []
    for player in players:
        positions.append(player.position)
    balances = []
    for player in players:
        balances.append(player.cash)
    properties = []
    for player in players:
        p_props = []
        for prop in player.properties:
            p_props.append(prop)
        properties.append(p_props)
    cards_drawn = []
    for player in players:
        p_cards = []
        for card in player.cards:
            p_cards.append(card)
        cards_drawn.append(p_cards)

    print("Round:")
    print("Positions:")
    for position in positions:
        print(position)
    print("Balances:")
    for balance in balances:
        print(balance)
    print("Properties:")
    for player in properties:
        for prop in player:
            print(prop.property_name)
    print("Cards Drawn:")
    for player in cards_drawn:
        for card in player:
            print(card.name)
        

def generate_YAML_file():
    root = game_rounds["Monopoly Game"]
    for rnd in rounds:
        with open("game_template.yml", 'r') as stream:
            temp = yaml.safe_load(stream)
            print(temp)


gameLoop()

gameLoop()

#generate_YAML_file()

