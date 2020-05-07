from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# List of objects and assigned rooms

torch = Item('Torch', 'A flaming torch for light and warmth')
sword = Item('Sword', 'A old rusty sword dropped by a previous adventurer')
coin = Item('Coin', 'Coin used for purchasing goods and services')
bow = Item('Bow', 'Bow for when you want to stab someone who is far away from you')

room['outside'].add_item(torch)
room['foyer'].add_item(sword)
room['narrow'].add_item(coin)
room['overlook'].add_item(bow)

action = ['Get', 'Drop']

# Make a new player object that is currently in the 'outside' room.

name = input("Please enter your player name: ")
player = Player(name, room['outside'], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print('You are currently in', player.location.name)
print(player.location.description)
print(f'You find {player.location.items[0].description}')


while True:
    cmd = input(
        "Please enter a direction you would like to travel in.... \n [I] - Inventory \n [n] - North \n [e] - East \n [s] - South \n [w] - West, \n or press q to quit the game: ")

    if cmd == 'n':
        # If player.location.n_to is NOT "NONE", then assign player.location.n_to (foyer) the current location.
        if player.location.n_to is not None:
            player.location = player.location.n_to
            print(
                f'You are now in {player.location.name}, {player.location.description}')
        else:
            print('You cannot go that way!')
        if player.location.items != []:
            for v in player.location.items:
                print(f'You find {v.description}')
                i = input(
                    f'Would you like to pick up the {v.name}? [Get] [Item-name]: ')
                if i == f'{action[0]} {player.location.items[0].name}':
                    player.pick_item(player.location.items[0])
                    print(
                        f'You have picked up the {player.location.items[0].name}!')
                    player.location.remove_item(player.location.items[0])
        else:
            print('The room is empty!')
    elif cmd == 'e':
        if player.location.e_to is not None:
            player.location = player.location.e_to
            print(
                f'You are now in {player.location.name}, {player.location.description}')
        else:
            print('You cannot go that way!')
        if player.location.items != []:
            for v in player.location.items:
                print(f'You find {v.description}')
                i = input(
                    f'Would you like to pick up the {player.location.items[0].name}? [Get] [Item-name]: ')
            if i == f'{action[0]} {player.location.items[0].name}':
                player.pick_item(player.location.items[0])
                print(
                    f'You have picked up the {player.location.items[0].name}!')
                player.location.remove_item(player.location.items[0])
        else:
            print('The room is empty!')
    elif cmd == 's':
        if player.location.s_to is not None:
            player.location = player.location.s_to
            print(
                f'You are now in {player.location.name}, {player.location.description}')
        else:
            print('You cannot go that way!')
        if player.location.items != []:
            for v in player.location.items:
                print(f'You find {v.description}')
                i = input(
                    f'Would you like to pick up the {player.location.items[0].name}? [Get] [Item-name]: ')
            if i == f'{action[0]} {player.location.items[0].name}':
                player.pick_item(player.location.items[0])
                print(
                    f'You have picked up the {player.location.items[0].name}!')
                player.location.remove_item(player.location.items[0])
        else:
            print('The room is empty!')
    elif cmd == 'w':
        if player.location.w_to is not None:
            player.location = player.location.w_to
            print(
                f'You are now in {player.location.name}, {player.location.description}')
        else:
            print('You cannot go that way!')
        if player.location.items != []:
            for v in player.location.items:
                print(f'You find {v.description}')
                i = input(
                    f'Would you like to pick up the {player.location.items[0].name}? [Get] [Item-name]: ')
            if i == f'{action[0]} {player.location.items[0].name}':
                player.pick_item(player.location.items[0])
                print(
                    f'You have picked up the {player.location.items[0].name}!')
                player.location.remove_item(player.location.items[0])
        else:
            print('The room is empty!')
    elif cmd == 'q':
        exit()
    elif cmd == 'I':
        if player.inventory != []:
            [print(s.name) for s in player.inventory]
            d = input('Please select an item to remove: ')
            for i in player.inventory:
                if i.name == d:
                    player.drop_item(i)
                    print(f'You have dropped the {i.name}!')
                    player.location.add_item(i)
            [print(j.name) for j in player.inventory]
        elif player.inventory == []:
            print('Your inventory is empty!')
    else:
        print('You must choose either [n] [s] [e] [w]!')
