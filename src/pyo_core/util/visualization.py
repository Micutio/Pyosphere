"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants
from cab_core.util.cab_visualization import Visualization

import pygame
import numpy
import math

# Author Tag
__author__ = 'Michael Wagner'

# Code
class Visualizer(Visualization):
    def __init__(self, c, screen):
        super().__init__(c, screen)

    def clone(self, cab_sys):
        return Visualizer(self.gc, cab_sys)

    def draw_agent(self, agent):
        if agent.x != None and agent.y != None and not agent.dead:
            radius = int(agent.size / 2)
            pygame.draw.circle(self.surface, agent.x, agent.y, radius, (0, 0, 0))

    def draw_cell(self, cell):
        """
        Simple exemplary visualization. Draw cell in white.
        """
        if cell is None:
            pass
        else:
            if cell.altitude > 10:
                red = 255
                green = 255
                blue = 255
            elif cell.altitude >= 0:
                red = 255 - cell.altitude * 20
                green = 255 - cell.altitude * 25
                blue = 0
            elif cell.altitude >= -10:
                red = max(220 + cell.altitude * 25, 0)
                green = max(230 + cell.altitude * 20, 0)
                blue = max(250 + cell.altitude * 20, 0)
                # blue = min(cell.altitude * -25, 255)
            else:
                red = 0
                green = 0
                blue = 100
            pygame.gfxdraw.filled_polygon(self.surface, cell.get_corners(), (red, green, blue))
            pygame.gfxdraw.aapolygon(self.surface, cell.get_corners(), (255, 255, 255))
            # pygame.draw.aalines(self.surface, (255, 255, 255), True, cell.get_corners(), True)

    def highlight(self, cell):
        """
        Simple exemplary visualization. Draw cell in white.
        """
        counter = 0
        for neigh in cell.neighbors:
            counter += 1
            crnrs = neigh.get_corners()
            # pygame.draw.aalines(self.surface, (255, 255, 255), True, crnrs, 0)
            # pygame.gfxdraw.filled_polygon(self.surface, crnrs, (0, 0, 0))
            pygame.gfxdraw.filled_polygon(self.surface, crnrs, (255, 255, 0))
        crnrs = cell.get_corners()
        pygame.gfxdraw.filled_polygon(self.surface, crnrs, (60, 200, 0))