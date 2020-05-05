# coding: utf-8
from typing import Any

from model.direction import Direction


class Cube:

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.side_free = {}
        for dir in Direction:
            self.side_free[dir] = True
        # the down side of a cube is always occupied either by the floor, either by another cube
        self.side_free[Direction.DOWN] = False

    def set_direction(self, direction: Direction, value: bool):
        self.side_free[direction] = value

    def get_direction(self, direction: Direction):
        return self.side_free[direction]

    def occupied_side(self, direction):
        self.set_direction(direction, False)

    def is_side_free(self, direction):
        return self.side_free[direction]

    def __str__(self) -> str:
        return 'Cube:[' + str(self.position) + " = " + str(self.color) + "]"
