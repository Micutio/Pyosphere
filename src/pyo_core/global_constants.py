"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants

import pygame
import numpy
import math

# Author Tag
__author__ = 'Michael Wagner'

# Code
class GC(GlobalConstants):
    def __init__(self):
        super().__init__()
        self.VERSION = 'version: 09-2015'
        self.TITLE = 'Pyosphere'
        ################################
        #     SIMULATION CONSTANTS     #
        ################################
        self.RUN_SIMULATION = False
        self.ONE_AGENT_PER_CELL = False
        ################################
        #         CA CONSTANTS         #
        ################################
        self.USE_HEX_CA = True
        self.USE_MOORE_NEIGHBORHOOD = True
        self.USE_CA_BORDERS = True
        self.DIM_X = 125  # How many cells is the ca wide?
        self.DIM_Y = 75  # How many cells is the ca high?
        self.CELL_SIZE = 9  # How long/wide is one cell?
        self.GRID_WIDTH = self.DIM_X * self.CELL_SIZE
        self.GRID_HEIGHT = self.DIM_Y * self.CELL_SIZE
        ################################
        #        ABM CONSTANTS         #
        ################################
        ################################
        #      UTILITY CONSTANTS       #
        ################################
        self.VIS_CELL_OPTIONS = ["altitude", "air", "water", "light", "value"]
        self.VIS_CELL_CURRENT = "altitude"