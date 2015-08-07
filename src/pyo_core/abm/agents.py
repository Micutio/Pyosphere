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

# Author Tag
__author__ = 'Michael Wagner'

# Code
class SuperAgent(CabAgent):
    """
    Special Agent class that handles creation and monitoring
    of the actual Pyosphere agents.
    """
    def __init__(self, x, y, gc):
        super().__init__(None, None, gc)

    def clone(self, x, y):
        return Agent(x, y, self.gc)

    def perceive_and_act(self, ca, abm):
        print("implement agent behavior here")

        # TODO: spawn cell agents periodically


class PyoAgent(CabAgent):
    """
    Parent class for all agents.
    Every subclass has to implement the perceive_and_act() method.
    """
    def __init__(self, x, y, gc):
        super().__init__(None, None, gc)
        self.cells = []

    def clone(self, x, y):
        return Agent(x, y, self.gc)

    def perceive_and_act(self, ca, abm):
        print("implement agent behavior here")