"""
Module Description
"""

# Imports
from cab.cab_global_constants import GlobalConstants
from cab.ca.cab_ca_hex import CellHex

import pygame
import numpy
import math
import random
# random.seed("FOOBAR")

# Author Tag
__author__ = 'Michael Wagner'

# Code
class PyoHexCell(CellHex):
    def __init__(self, x, y, c):
        super().__init__(x, y, c)
        self.altitude = 0
        self.air = 0
        self.water = 0
        self.light = 0
        self.t_gen = None
        

    def sense_neighborhood(self):
        pass
        #print('implement cell behavior')

    def set_terrain_gen(self, tg):
        self.t_gen = tg
        self.altitude = self.t_gen.get(self.x, self.y)
        if self.altitude >= 0:
            self.air = max(10 - self.altitude, 0)
            self.water = 0 #max(6 - self.altitude, 0)
            self.light = min(self.altitude, 10)
        else:
            self.air = 0
            self.water = 10
            self.light = max(self.altitude + 3, 0)

    def update(self):
        pass

    def clone(self, x, y, gc):
        pc = PyoHexCell(x, y, gc)
        pc.set_terrain_gen(self.t_gen)
        return pc


class TerrainGenerator():
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim * 2
        self.y_dim = y_dim * 2
        self.highest = 20
        self.deepest = -20
        self.slope = 1.0
        self.smoothness = 2
        self.water_level = 0
        self.landscape = None
        self.factor = 10
        self.landscape = self.get_island_landscape()
        
        # self.landscape = self.get_coastal_landscape()

    def get(self, x, y):
        offset_x = int(self.x_dim / 2)
        offset_y = int(self.y_dim / 2)
        return self.landscape[x + offset_x][y + offset_y]

    def get_coastal_landscape(self):
        l1 = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        l2 = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        for j in range(self.y_dim):
            for i in range(self.x_dim):
                # l1[i][j] = int(random.triangular(self.deepest, self.highest, 5))s
                mode = (((i + j) / 200) * 20) - 15
                l1[i][j] = int(random.triangular(self.deepest + 2 * mode, self.highest + 2 * mode, mode))

        for _ in range(self.smoothness):
            for j in range(self.y_dim):
                for i in range(self.x_dim):
                    n = 0
                    f = 0
                    for cy in range(-1, 2):
                        for cx in range(-1, 2):
                            if not (cy == 0 and cx == 0):
                                try:
                                    n += 1
                                    f += l1[i + cx][j + cy]
                                except IndexError:
                                    pass
                    avg = f / n
                    if avg > l1[i][j]:
                        diff = avg - l1[i][j]
                        l2[i][j] = l1[i][j] + (diff * self.slope)
                    elif avg < l1[i][j]:
                        diff = l1[i][j] - avg
                        l2[i][j] = l1[i][j] - (diff * self.slope)
                    else:
                        l2[i][j] = l1[i][j]
            l1, l2 = l2, l1
        return l1

    def get_island_landscape(self):
        l1 = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        l2 = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        lower_limit  = int((self.y_dim + self.x_dim) * 0.33)
        upper_limit  = int((self.y_dim + self.x_dim) * 0.9)
        print(lower_limit, upper_limit)
        last_rand = 0
        for j in range(self.y_dim):
            for i in range(self.x_dim):
                if (i + j) % self.factor == 0:
                    last_rand = int(random.triangular(self.deepest, self.highest, self.water_level))
                l1[i][j] = last_rand

        for _ in range(self.smoothness):
            for j in range(self.y_dim):
                for i in range(self.x_dim):
                    n = 0
                    f = 0
                    for cy in range(-1, 2):
                        for cx in range(-1, 2):
                            if not (cy == 0 and cx == 0):
                                try:
                                    n += 1
                                    f += l1[i + cx][j + cy]
                                except IndexError:
                                    pass
                    avg = f / n
                    if avg > l1[i][j]:
                        diff = avg - l1[i][j]
                        l2[i][j] = l1[i][j] + (diff * self.slope)
                    elif avg < l1[i][j]:
                        diff = l1[i][j] - avg
                        l2[i][j] = l1[i][j] - (diff * self.slope)
                    else:
                        l2[i][j] = l1[i][j]
            l1, l2 = l2, l1
        return l1
