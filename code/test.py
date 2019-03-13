import numpy as np
import csv

#------------------------------------------------------------------------------
# Class definitions

# Create a class for a tile.
class tileClass:

    def setData(self, attributes):
        self.name = attributes[0]
        self.north = attributes[1]
        self.east = attributes[2]
        self.south = attributes[3]
        self.west = attributes[4]

    def display(self):
        print(self.north)

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Setup the game

# Create an empty list of tiles
tiles = []

# Read the set of tiles
with open('../tiles/tile_descriptions.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:

        tile = tileClass()
        tile.setData(row)
        tiles.append(tile)

#------------------------------------------------------------------------------
# Play the game

playersTiles = [[], [], []]

turn = 0
while tiles.__len__() > 0:

    player = 0
    while player < playersTiles.__len__():  
        
        # Player one draws a tile, makes a decision as to where to place it, and
        # makes a decision if to place a meeple or not.

        # Draw a tile
        drawnTile = np.random.choice(tiles.__len__())
        playersTiles[player].append(tiles[drawnTile])
        tiles.pop(drawnTile)

        # Decide where to place the tile

        # Decide if to place a meeple or not

        # If there are no tiles remaining, but not all the players have selected
        # a tile this turn, then break and the game is done; else, move to the next
        # player
        if tiles.__len__() == 0:
            break
        else:
            player = player + 1

    # Increment the turn counter
    turn = turn + 1
    



