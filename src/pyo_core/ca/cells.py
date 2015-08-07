"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants
from cab_core.ca.cab_ca_hex import CellHex

import pygame
import numpy
import math

# Author Tag
__author__ = 'Michael Wagner'

# Code
class PyoHexCell(CellHex):
    def __init__(self, x, y, c_size, c):
        super().__init__(x, y, c_size, c)
        self.altitude = ((x + y) - 20)

    def sense_neighborhood(self):
        pass
        #print('implement cell behavior')

    def update(self):
        pass

    def clone(self, x, y, c_size):
        return PyoHexCell(x, y, c_size, self.gc)