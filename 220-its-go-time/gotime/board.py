# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

class Board:

    def __init__(self, file):
        self.board = []
        self.load_from_file(file)

    def load_from_file(self, file):
        input_file = open(file, 'r')
        for i, line in enumerate(input_file):
            if i == 0:
                self.width, self.height = [int(dimension) for dimension in line.strip().split(' ')]
            elif i == 1:
                self.player = line.strip()
                self.opponent = 'w' if self.player == 'b' else 'b'
            else:
                points = list(line.rstrip().ljust(self.width))
                points = [{'player': None if point == ' ' else point, 'checked': False} for point in points]
                self.board.append(points)

        input_file.close()

        # fill in any missing empty lines from the txt file
        for fillLine in range(self.height - len(self.board)):
            self.board.append(list(''.ljust(self.width)))

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
                    logger.debug("Skipping {0},{1}".format(j, i))
                    pass

        # stones = self.opponent_stones()
        # print stones
        return [0, 0]