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
        self.cells = {}
        self.energy = 0
        self.age = 0

    def perceive_and_act(self, ca, abm):
        # print("implement plant agent behavior here")
        if not self.dead:
            if self.age == 100:
                self.dead = True
            else:
                self.age += 1
                self.energy += self.gain_from_cell(ca.ca_grid[self.x, self.y])
                # if energy high enough, spawn offspring in [most fitting/random] neighboring cell
                # determine how much energy is given to the offspring
                # and how much used by self every turn.

    def gain_from_cell(self, cell):
        total_gain = 0
        for c in self.cells[0]:
            total_gain += cell.air * c
        for c in self.cells[1]:
            total_gain += cell.water * c
        for c in self.cells[2]:
            total_gain += cell.light * c
        return total_gain

    def decode_genes(self):
        # int = int(string, 2)
        # bit 0,1 : type of cell
        # bit 2 .. 5 : efficiency or preferred value?
        # Idea: make energy consumption dependent on total number of cells
        # Idea: multiplicator if food gathered from multiple different resources
        for i in range(0, len(self.genome), 100):
            chunk = self.genome[i:i + 6]
            cell_type = int(chunk[:2], 2)
            efficiency = int(chunk[2:6], 2)
            if cell_type in self.cells:
                self.cells[cell_type].append(efficiency)
            else:
                self.cells[cell_type] = [efficiency]
        # Use print(''.join(random.choice('0', '1') for i in range(x * 6)))