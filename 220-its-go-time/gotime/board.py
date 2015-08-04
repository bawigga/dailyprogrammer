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

    def scan(self, i, j):
        point = self.board[i][j]
        liberties = []
        connected_stones = 0
        logger.debug("[{0},{1}] - {2}".format(i, j, point))

        if(point['player'] is None):
            return [[i, j]], connected_stones

        if(point['checked'] == True):
            return [], connected_stones
        else:
            point['checked'] = True

        if(point['player'] == self.player):
            return [], connected_stones
        elif(point['player'] == self.opponent):
            if i > 0:
                child_liberties, child_stones = self.scan(i - 1, j)
                liberties = liberties + child_liberties
                connected_stones += child_stones
            # right
            if j < self.width-1:
                child_liberties, child_stones = self.scan(i, j + 1)
                liberties = liberties + child_liberties
                connected_stones += child_stones
            # bottom
            if i < self.height-1:
                child_liberties, child_stones = self.scan(i+1, j)
                liberties = liberties + child_liberties
                connected_stones += child_stones
            # left
            if j > 0:
                child_liberties, child_stones = self.scan(i, j-1)
                liberties = liberties + child_liberties
                connected_stones += child_stones

            # remove black libs
            liberties = [x for x in liberties if x]
            logger.debug("[{0},{1}] - liberties {2}".format(i, j, liberties))
            logger.debug("[{0},{1}] - connected_stones {2}".format(i, j, connected_stones))
            return liberties, connected_stones + 1

    def solve(self):
        solutions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                player = self.board[i][j]['player']
                if player is None:
                    logger.debug("[{0},{1}] - Empty".format(i, j))
                    pass
                elif player == self.player:
                    logger.debug("[{0},{1}] - {2}".format(i, j, "Black" if self.board[i][j]['player'] == 'b' else "White"))
                    pass
                else:
                    logger.debug("[{0},{1}] - {2}".format(i, j, "Black" if self.board[i][j]['player'] == 'b' else "White"))
                    logger.debug('--- SCAN ---')
                    liberties, connected_stones = self.scan(i, j)
                    logger.debug('------------')
                    if len(liberties) == 1:
                        solutions.append({"point": liberties[0], "captured_stones": connected_stones})
        return sorted(solutions)
