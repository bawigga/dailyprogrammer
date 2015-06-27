# -*- coding: utf-8 -*-

import sys
import logging
from pprint import pprint

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger('GOTIME')


class Point:
    def __init__(self, x, y, owner=None):
        self.x = x
        self.y = y
        self.owner = owner


class Board:

    BLACK_CHAR = '◎'
    WHITE_CHAR = '◉'

    GRID_TL = '┏'
    GRID_TR = '┓'
    GRID_BL = '┗'
    GRID_BR = '┛'
    GRID_T_WALL = '┳'
    GRID_B_WALL = '┻'
    GRID_L_WALL = '┣'
    GRID_R_WALL = '┫'
    GRID_CROSS = '╋'

    def __init__(self, file):
        f = open(file, 'r')
        self.board = []
        for i, line in enumerate(f):
            if i == 0:
                self.width, self.height = [int(dimension) for dimension in line.strip().split(' ')]
            elif i == 1:
                self.player = line
            else:
                self.board.append(list(line.rstrip().ljust(self.width)))
        f.close()

    def get_grid_char(self, x, y):
        # top line
        if y == 0:
            if x == 0:
                return self.GRID_TL
            elif x == self.width - 1:
                return self.GRID_TR
            else:
                return self.GRID_T_WALL
        # bottom line
        elif y == self.height - 1:
            if x == 0:
                return self.GRID_BL
            elif x == self.width - 1:
                return self.GRID_BR
            else:
                return self.GRID_B_WALL
        # everything else
        else:
            # left wall
            if x == 0:
                return self.GRID_L_WALL
            # right wall
            elif x == self.width - 1:
                return self.GRID_R_WALL
            # inner point
            else:
                return self.GRID_CROSS
            pass

        return ' '

    def __str__(self):
        str = ''
        for y in range(self.height):
            for x in range(self.width):
                point = self.board[y][x]
                if point == 'b':
                    str = str + self.BLACK_CHAR
                elif point == 'w':
                    str = str + self.WHITE_CHAR
                else:
                    str = str + self.get_grid_char(x, y)
                str = str + ' '
            str = str + '\n'
        return str


board = Board('scenario.txt')

print board
