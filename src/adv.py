from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     (Item('Rock', 'Fist size piece of granite.'))),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ()), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ()),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ()),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ()),
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

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

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

location = player.room
print('\n')
print(room[location])
print('\n')
move = input('What direction do you want to go? (North, South, East, West, or quit) ')

while not move == 'quit':
    if location == 'outside':
        if move == 'North':
            player.room = 'foyer'
        elif move == 'South' or 'East' or 'West':
            print(f'\n You cannot move {move}')
        else:
            print(f'\n I dont understand {move}, please select again.')
    elif location == 'foyer':
        if move == 'North':
            player.room = 'overlook'
        elif move == 'South':
            player.room = 'outside'
        elif move == 'East':
            player.room = 'narrow'
        elif move == 'West':
            print(f'\n You cannot move {move}')
        else:
            print(f'\n I dont understand {move}, please select again.')
    elif location == 'overlook':
        if move == 'South':
            player.room = 'foyer'
        elif move == 'North' or 'East' or 'West':
            print(f'\n You cannot move {move}')
        else:
            print(f'\n I dont understand {move}, please select again.')
    elif location == 'narrow':
        if move == 'North':
            player.room = 'treasure'
        elif move == 'West':
            player.room = 'foyer'
        elif move == 'South' or 'East':
            print(f'\n You cannot move {move}')
        else:
            print(f'\n I dont understand {move}, please select again.')
    elif location == 'treasure':
        if move == 'South':
            player.room = 'narrow'
        elif move == 'North' or 'East' or 'West':
            print(f'\n You cannot move {move}')
        else:
            print(f'\n I dont understand {move}, please select again.')

    location = player.room
    print('\n')
    print(room[location])
    print('\n')
    move = input('What direction do you want to go? (North, South, East, West, or quit) ')