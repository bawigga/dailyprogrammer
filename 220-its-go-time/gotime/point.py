# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

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
