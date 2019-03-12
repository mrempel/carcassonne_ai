import numpy as np
import csv

class tileClass:

    def setData(self, attributes):
        self.name = attributes[0]
        self.north = attributes[1]
        self.east = attributes[2]
        self.south = attributes[3]
        self.west = attributes[4]

    def display(self):
        print(self.north)

# Create an empty list of tiles
tiles = []

with open('../tiles/tile_descriptions.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        print(row)

        tile = tileClass()
        tile.setData(row)
        tiles.append(tile)

tiles[20].display()
