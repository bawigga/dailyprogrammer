# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

class Goban:

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

    def __init__(self, board):
        self.board = board.board
        self.height = len(self.board)
        self.width = len(self.board[0])

    def __str__(self):
        str = ''
        for y in range(self.height):
            for x in range(self.width):
                point = self.board[y][x]
                if point['player'] == 'b':
                    str = str + self.BLACK_CHAR
                elif point['player'] == 'w':
                    str = str + self.WHITE_CHAR
                else:
                    str = str + self.get_grid_char(x, y)
                str = str + ' '
            str = str + '\n'
        return str

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
