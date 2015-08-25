"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants
from cab_core.abm.cab_agent import CabAgent

import pygame
import numpy
import math
import uuid
import random

# Author Tag
__author__ = 'Michael Wagner'

# Code
class GaiaAgent(CabAgent):
    """
    Special Agent class that handles creation and monitoring
    of the actual Pyosphere agents.
    """
    def __init__(self, x, y, gc):
        super().__init__(None, None, gc)
        self.genome = []
        # inherited agent fields:
        #   self.a_id = uuid.uuid4().urn
        #   self.x = x
        #   self.y = y
        #   self.prev_x = x
        #   self.prev_y = y
        #   self.size = gc.CELL_SIZE
        #   self.gc = gc
        #   self.dead = False

    def clone(self, x, y):
        return Agent(x, y, self.gc)

    def perceive_and_act(self, ca, abm):
        if random.random() > 0.9:
            pass
        x = random.randint(0, self.gc.DIM_X)
        y = random.randint(0, self.gc.DIM_Y)
        q = x - math.floor(y / 2)
        abm.add_agent(PyoAgent(q, y, self.gc))
        print('[GaiaAgent] spawning new life form in {0}, {1}'.format(q, y))
        # TODO: spawn cell agents periodically


class PyoAgent(CabAgent):
    """
    Parent class for all agents.
    Every subclass has to implement the perceive_and_act() method.
    """
    def __init__(self, x, y, gc, gene_string):
        super().__init__(x, y, gc)
        self.genome = gene_string


    def perceive_and_act(self, ca, abm):
        # print("implement plant agent behavior here")
        pass

    def decode_genes(self):
        # int = int(string, 2)
        # bit 0,1 : type of cell
        # bit 2 .. 5 : efficiency or preferred value?
        pass

