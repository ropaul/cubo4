# coding: utf-8
from copy import copy

from model.color import Color
from model.direction import Direction
from model.point import Point
from model.cube import Cube
from model.sens import Sens


class Board:

    def __init__(self):
        self.player1 = "Ferrari"
        self.player2 = " autre"
        self.cases = {}

    def begin(self, color):
        point = Point(0, 0, 0)
        self.cases[point] = Cube(color, point)

    def play(self, color: Color, position: Point):
        if position in self.cases:
            return Exception('position is already taken')
        fresh_cube = Cube(color, position)
        self.cases[position] = fresh_cube
        surrounding_position = position.surrounding()
        for key, value in surrounding_position.items():
            if key in self.cases:
                fresh_cube.occupied_side(value)
                self.cases[key].occupied_side(value.get_inverse())
        return self.win(color, position)

    # to know if the player color has win with his last cube
    def win(self, color: Color, position: Point):
        for dir in Direction:
            for s in Sens:
                align = self.range(color, position, s, dir)
                if align >= 4:
                    return s, dir
        return False

    def range(self, color: Color, position: Point, direction_value: Sens, face: Direction):
        if direction_value == Sens.WIDTH:
            return self.aligned_faces(color, position, Direction.LEFT, face) + self.aligned_faces(color, position,
                                                                                                  Direction.RIGHT, face)
        if direction_value == Sens.DEPTH:
            return self.aligned_faces(color, position, Direction.BACKWARD, face) + self.aligned_faces(color, position,
                                                                                                      Direction.FORWARD,
                                                                                                      face)
        if direction_value == Sens.HEIGHT:
            return self.aligned_faces(color, position, Direction.DOWN, face) + self.aligned_faces(color,
                                                                                                  position,
                                                                                                  Direction.UP,
                                                                                                  face)

    # give the number of cube which the face is free with position a the beginning and following the direction
    def aligned_faces(self, color: Color, position: Point, direction: Direction, face: Direction):
        result = 0
        current_position = copy(position)
        while current_position in self.cases and self.cases[current_position].color == color \
                and self.cases[current_position].is_side_free(face):
            result += 1
            current_position += Point.direction(direction)
        return result

    def get_playable_position(self):
        playable_position = []
        for position in self.cases.keys():
            around = position.surrounding()
            for a in around:
                if not a in self.cases and a.above_the_table():
                    playable_position.append(a)
        return playable_position

    def __str__(self) -> str:
        s = ''
        for case in self.cases.values():
            s += str(case.position) + " = " + str(case.color) + "\n"
        return s
