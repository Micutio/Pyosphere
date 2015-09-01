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
import copy

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
        # print(''.join(random.choice(('0', '1')) for i in range(6)))
        if random.random() > 0.9:
            pass
        if len(abm.agent_locations) == 0:
            x = random.randint(0, self.gc.DIM_X)
            y = random.randint(0, self.gc.DIM_Y)
            q = x - math.floor(y / 2)
            genome = ''.join(random.choice(('0', '1')) for _ in range(6))
            abm.add_agent(PyoAgent(q, y, self.gc, genome))
            print('[GaiaAgent] spawning new life form in ({0}, {1}) with genome: {2}'.format(q, y, genome))
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
        self.complexity = 0
        self.energy = 10
        self.age = 0
        self.decode_genes()

    def perceive_and_act(self, ca, abm):
        # print("implement plant agent behavior here")
        if not self.dead:
            if self.age == 100 or self.energy <= 0:
                self.dead = True
                abm.remove_agent(self)
                # print('[plant agent] agent died')
            else:
                self.age += 1
                self.energy += self.gain_from_cell(ca.ca_grid[self.x, self.y])
                # print('gains: {0}, losses: {1}'.format(self.gain_from_cell(ca.ca_grid[self.x, self.y]), self.complexity))
                
                # if energy high enough, spawn offspring in [most fitting/random] neighboring cell
                # determine how much energy is given to the offspring
                # and how much used by self every turn.

                self.energy -= self.complexity * 2

                # print('current energy: {0}'.format(self.energy))
                if self.energy >= 50:
                    self.spawn_offspring(ca, abm)
                    self.energy -= 40


    def gain_from_cell(self, cell):
        total_gain = 0
        if 0 in self.cells:
            for c in self.cells[0]:
                gain = cell.air * c
                loss = cell.air * (1 - c)
                total_gain += (gain - loss)
        if 1 in self.cells:
            for c in self.cells[1]:
                gain = cell.water * c
                loss = cell.water * (1 - c)
                total_gain += (gain - loss)
        # if 2 in self.cells:
        #     for c in self.cells[2]:
        #         gain = cell.light * c
        #         loss = cell.light * (1 - c)
        #         total_gain += (gain - loss)
        return total_gain

    def decode_genes(self):
        # int = int(string, 2)
        # bit 0,1 : type of cell
        # bit 2 .. 5 : efficiency or preferred value?
        # Idea: make energy consumption dependent on total number of cells
        # Idea: multiplicator if food gathered from multiple different resources
        for i in range(0, len(self.genome), 6):
            chunk = self.genome[i:i + 6]
            cell_type = int(chunk[:2], 2)
            efficiency = int(chunk[2:6], 2) / 16
            print('cell_type: {0}, efficiency: {1}'.format(cell_type, efficiency))
            if cell_type in self.cells:
                self.cells[cell_type].append(efficiency)
            else:
                self.cells[cell_type] = [efficiency]
            self.complexity += 1

    def mutate_genes(self):
        result = self.genome
        # With very small likelihood, the genome will be doubled
        if random.random() < 0.001:
            result = result + result
            print('duplication occurred')
        # With certain likelihood, a bit in the genome will be flipped
        elif random.random() < 0.1:
            index = random.choice(range(len(self.genome)))
            l = list(result)
            l[index] = str(1 - int(l[index]))
            result = ''.join(l)
            print('mutation occurred')

        return result

    def spawn_offspring(self, ca, abm):
        neigh_cells = ca.get_empty_agent_neighborhood(abm.agent_locations, self.x, self.y, 1)
        pos = None
        max_gain = 0
        # for key in list(neigh_cells.keys()):
        #     if self.gain_from_cell(neigh_cells[key]) > max_gain:
        #         max_gain = self.gain_from_cell(neigh_cells[key])
        #         pos = key
        if len(list(neigh_cells.keys())) > 0:
            pos = random.choice(list(neigh_cells.keys()))
        if pos != None:
            abm.add_agent(PyoAgent(pos[0], pos[1], self.gc, self.mutate_genes()))
            # print('spawned new plant at ({0}, {1})'.format(pos[0], pos[1]))