"""
Module Description
"""

# Imports
from cab_core.cab_global_constants import GlobalConstants
from cab_core.util.cab_input_handling import InputHandler

import pygame
import numpy
import math

# Author Tag
__author__ = 'Michael Wagner'

# Code

def hex_round(q, r):
    return cube_to_hex(*cube_round(*hex_to_cube(q, r)))

def cube_round(x, y, z):
    rx = round(x)
    ry = round(y)
    rz = round(z)
    dx = abs(rx - x)
    dy = abs(ry - y)
    dz = abs(rz - z)

    if dx > dy and dx > dz:
        rx = -ry - rz
    elif dy > dz:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return rx, ry, rz

def cube_to_hex(x, y, z):
    return x, y

def hex_to_cube(q, r):
    z = -q - r
    return q, r, z


class InputHandler(InputHandler):
    def __init__(self, cab_sys):
        super().__init__(cab_sys)

    def clone(self, cab_sys):
        return InputHandler(cab_sys)

    def get_mouse_hex_coords(self):
        _q = (self.mx * math.sqrt(3)/3 - self.my/3)# / self.sys.gc.CELL_SIZE
        _r = self.my * 2/3# / self.sys.gc.CELL_SIZE
        cell_q, cell_r = hex_round(_q, _r)
        return cell_q, cell_r

    # def custom_mouse_motion(self):
    #     '''
    #     Converts mouse cursor position from pixel to hex
    #     and colors the cell it currently hovers.
    #     '''
    #     _q = (self.mx * math.sqrt(3)/3 - self.my/3)# / self.sys.gc.CELL_SIZE
    #     _r = self.my * 2/3# / self.sys.gc.CELL_SIZE
    #     cell_q, cell_r = hex_round(_q, _r)
    #     # print('raw coordinates: ({0}, {1})'.format(_q, _r))
    #     # print('cell coordinates: ({0}, {1})'.format(cell_q, cell_r))
    #     if (cell_q, cell_r) in self.sys.ca.ca_grid:
    #         self.sys.visualizer.highlight(self.sys.ca.ca_grid[cell_q, cell_r])

    def custom_mouse_action(self, button):
        # Click on left mouse button.
        if button == 1:
            cell_x, cell_y = self.get_mouse_hex_coords()
            c = self.sys.ca.ca_grid[cell_x, cell_y]
            print('leftclicking cell ({0},{1})'.format(cell_x, cell_y))
            print('altitude: {0}\n'
                  'air:      {1}\n'
                  'water:    {2}\n'
                  'light:    {3}\n'
                  'value:    {4}'.format(c.altitude, c.air, c.water, c.light, c.air + c.water + c.light))
            # self.sys.ca.ca_grid[cell_x, cell_y].altitude += 1

        # Click on middle mouse button / mouse wheel
        elif button == 2:
            cell_x, cell_y = self.get_mouse_hex_coords()
            print('middleclicking cell ({0},{1})'.format(cell_x, cell_y))

        # Click on right mouse button
        elif button == 3:
            cell_x, cell_y = self.get_mouse_hex_coords()
            print('rightclicking cell ({0},{1})'.format(cell_x, cell_y))
            # self.sys.ca.ca_grid[cell_x, cell_y].altitude -= 1



    def custom_keyboard_action(self, active_key):
        """
        Customizable Method to process keyboard inputs.
        Overwrite this method to add more inputs.
        """
        if active_key == pygame.K_1:
            self.sys.gc.VIS_CELL_CURRENT = self.sys.gc.VIS_CELL_OPTIONS[0]
            print("cell visualization: {0}".format(self.sys.gc.VIS_CELL_OPTIONS[0]))
        elif active_key == pygame.K_2:
            self.sys.gc.VIS_CELL_CURRENT = self.sys.gc.VIS_CELL_OPTIONS[1]
            print("cell visualization: {0}".format(self.sys.gc.VIS_CELL_OPTIONS[1]))
        elif active_key == pygame.K_3:
            self.sys.gc.VIS_CELL_CURRENT = self.sys.gc.VIS_CELL_OPTIONS[2]
            print("cell visualization: {0}".format(self.sys.gc.VIS_CELL_OPTIONS[2]))
        elif active_key == pygame.K_4:
            self.sys.gc.VIS_CELL_CURRENT = self.sys.gc.VIS_CELL_OPTIONS[3]
            print("cell visualization: {0}".format(self.sys.gc.VIS_CELL_OPTIONS[3]))
        elif active_key == pygame.K_5:
            self.sys.gc.VIS_CELL_CURRENT = self.sys.gc.VIS_CELL_OPTIONS[4]
            print("cell visualization: {0}".format(self.sys.gc.VIS_CELL_OPTIONS[4]))