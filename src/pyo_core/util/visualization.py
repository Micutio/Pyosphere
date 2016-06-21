"""
Module Description
"""

# Imports
from cab.cab_global_constants import GlobalConstants
from cab.util.cab_visualization import Visualization

import pygame
import numpy
import math

# Author Tag
__author__ = 'Michael Wagner'

# Code
class Visualizer(Visualization):
    def __init__(self, gc, screen, sys):
        super().__init__(gc, screen, sys)

    def clone(self, gc, surface, cab_sys):
        return Visualizer(gc, surface, cab_sys)

    def draw_agent(self, agent):
        # print(agent.x, agent.y)
        if agent.x != None and agent.y != None and not agent.dead:
            radius = int(agent.size / 1.5)

            horiz = self.gc.CELL_SIZE * 2 * (math.sqrt(3) / 2)
            offset = agent.y * (horiz / 2)
            x = int(agent.x * horiz) + int(offset)

            vert = self.gc.CELL_SIZE * 2 * (3 / 4)
            y = int(agent.y * vert)
            
            pygame.draw.circle(self.surface, (0, 255, 0), (x, y), radius, 0)
            pygame.gfxdraw.aacircle(self.surface, x, y, radius, (50, 100, 50))
            # corners = [(x - radius, y - radius), (x + radius, y - radius), (x + radius, y + radius), (x - radius, y + radius), (x - radius, y - radius)]
            # pygame.gfxdraw.filled_polygon(self.surface, corners, (0, 255, 0))
            # pygame.gfxdraw.aapolygon(self.surface, corners, (0, 100, 0))

    def draw_cell(self, cell):
        """
        Simple exemplary visualization. Draw cell in white.
        """
        if cell is None:
            return
        elif self.gc.VIS_CELL_CURRENT == "altitude":
            if cell.altitude > 10:
                red = 255
                green = 255
                blue = 255
            elif cell.altitude >= 0:
                red = 255 - cell.altitude * 20
                green = 255 - cell.altitude * 25
                blue = 0
            elif cell.altitude >= -10:
                red = max(180 + cell.altitude * 25, 0)
                green = max(240 + cell.altitude * 20, 0)
                blue = max(250 + cell.altitude * 20, 0)
                # blue = min(cell.altitude * -25, 255)
            else:
                red = 0
                green = 0
                blue = 100
        elif self.gc.VIS_CELL_CURRENT == "air":
            blue = int(cell.air / 10 * 255)
            red = int(blue * 0.6)
            green = 0
        elif self.gc.VIS_CELL_CURRENT == "water":
            blue = green = int(cell.water / 10 * 255)
            red = 0
        elif self.gc.VIS_CELL_CURRENT == "light":
            red = green = int(cell.light / 10 * 255)
            blue = 0
        elif self.gc.VIS_CELL_CURRENT == "value":
            red = green = blue = int((cell.air + cell.water + cell.light) / 30 * 255)
        
        pygame.gfxdraw.filled_polygon(self.surface, cell.corners, (red, green, blue))
        pygame.gfxdraw.aapolygon(self.surface, cell.corners, (255, 255, 255))
        # pygame.draw.aalines(self.surface, (255, 255, 255), True, cell.corners, True)

    def highlight(self, cell):
        """
        Simple exemplary visualization. Draw cell in white.
        """
        counter = 0
        for neigh in cell.neighbors:
            counter += 1
            crnrs = neigh.corners
            # pygame.draw.aalines(self.surface, (255, 255, 255), True, crnrs, 0)
            # pygame.gfxdraw.filled_polygon(self.surface, crnrs, (0, 0, 0))
            pygame.gfxdraw.filled_polygon(self.surface, crnrs, (255, 255, 0))
        crnrs = cell.corners
        pygame.gfxdraw.filled_polygon(self.surface, crnrs, (60, 200, 0))
