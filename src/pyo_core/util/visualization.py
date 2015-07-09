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

    def draw_cell(self, cell):
        """
        Simple exemplary visualization. Draw cell in white.
        """
        if cell is None:
            pass
        else:
            if cell.altitude >= 0:
                red = int((cell.altitude / 10) * 255)
                green = int((cell.altitude / 10) * 255)
                blue = 150 - int((cell.altitude / 10) * 150)
            else:
                red = 150 - int((cell.altitude / 10) * 150)
                green = 150 - int((cell.altitude / 10) * 150)
                blue = int((cell.altitude / 10) * 255)
            pygame.gfxdraw.filled_polygon(self.surface, cell.get_corners(), (red, green, blue))
            pygame.gfxdraw.aapolygon(self.surface, cell.get_corners(), (255, 255, 255))

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