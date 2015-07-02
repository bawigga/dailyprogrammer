# -*- coding: utf-8 -*-

import sys
import logging


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger('GOTIME')


class Point:
    def __init__(self, i, j, owner, top, right, bottom, left):
        self.i = i
        self.j = j
        self.owner = owner

        # liberties
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def in_atari(self):
        if self.top:
            if self.top.owner is None:
                count += 1

        if self.right:
            if self.right.owner is None:
                count += 1

        if self.bottom:
            if self.bottom.owner is None:
                count += 1

        if self.left:
            if self.left.owner is None:
                count += 1

    def has_liberties(self):
        count = 0

        if self.top:
            if self.top.owner is None:
                count += 1

        if self.right:
            if self.right.owner is None:
                count += 1

        if self.bottom:
            if self.bottom.owner is None:
                count += 1

        if self.left:
            if self.left.owner is None:
                count += 1


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
        self.board = []
        self.load_from_file(file)

    def load_from_file(self, file):
        input_file = open(file, 'r')
        for i, line in enumerate(input_file):
            if i == 0:
                self.width, self.height = [int(dimension) for dimension in line.strip().split(' ')]
            elif i == 1:
                self.player = line
                self.opponent = 'b' if self.player == 'b' else 'w'
            else:
                points = list(line.rstrip().ljust(self.width))
                points = [{'player': None if point == ' ' else point, 'checked': False} for point in points]
                self.board.append(points)

        input_file.close()

        # fill in any missing empty lines from the txt file
        for fillLine in range(self.height - len(self.board)):
            self.board.append(list(''.ljust(self.width)))

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
                if point['player'] == 'b':
                    str = str + self.BLACK_CHAR
                elif point['player'] == 'w':
                    str = str + self.WHITE_CHAR
                else:
                    str = str + self.get_grid_char(x, y)
                str = str + ' '
            str = str + '\n'
        return str

    def _opponent_stones(self):
        points = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.opponent:
                    points.append([i, j])
        return points

    def solve(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j]['checked'] = True
                # skip empty spaces
                if self.board[i][j]['player'] is None:
                    pass

        # stones = self.opponent_stones()
        # print stones
        return [0, 0]


board = Board('scenario.txt')

print board
print board.solve()
