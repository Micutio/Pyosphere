"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants

import pygame
import numpy
import math
import uuid

# Author Tag
__author__ = 'Michael Wagner'

# Code
class PyoAgent:
    """
    Parent class for all agents.
    Every subclass has to implement the perceive_and_act() method.
    """
    def __init__(self, x, y, gc):
        self.a_id = uuid.uuid4().urn
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.size = gc.CELL_SIZE
        self.gc = gc
        self.dead = False

    def clone(self, x, y):
        return Agent(x, y, self.gc)

    def perceive_and_act(self, ca, abm):
        print("implement agent behavior here")