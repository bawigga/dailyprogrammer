# -*- coding: utf-8 -*-
import logging
import sys

from gotime.goban import Goban
from gotime.board import Board

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    board = Board('scenario.txt')
    print Goban(board)
    print "{0}'s turn!\n".format('White' if board.player == 'w' else 'Black')
    print board.solve()

if __name__ == '__main__':
    main()
