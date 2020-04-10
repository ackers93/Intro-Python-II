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

room['outside'].items.append(torch)
room['foyer'].items.append(sword)
room['narrow'].items.append(coin)
room['overlook'].items.append(bow)

# Make a new player object that is currently in the 'outside' room.

player = Player(input("Input your name:"), room['outside'])
print(f'Welcome, {player.name}')
print(player.current_room.description)

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


game = True

while game:
    command = input(
        'chose n for north, e for east, s for south and w for west, or q to quit.')
    if command == 'n':
        player.move(command)

    elif command == 'e':
        player.move(command)

    elif command == 's':
        player.move(command)

    elif command == 'w':
        player.move(command)

    elif command == 'i':
        player.inventory_list()

    elif command == 'take':
        item = command.split(' ')[0]
        player.take(item)
        player.inventory_list()

    elif command == 'drop':
        item = command.split(' ')[0]
        player.drop(item)
        player.inventory_list()

    elif command == 'q':
        game = False

    else:
        print("Try something else")
