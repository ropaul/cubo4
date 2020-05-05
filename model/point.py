# coding: utf-8
from model.direction import Direction


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def surrounding(self):
        return {Point(self.x - 1, self.y, self.z): Direction.LEFT,
                Point(self.x + 1, self.y, self.z): Direction.RIGHT,
                Point(self.x, self.y - 1, self.z): Direction.BACKWARD,
                Point(self.x, self.y + 1, self.z): Direction.FORWARD,
                Point(self.x, self.y, self.z - 1): Direction.DOWN,
                Point(self.x, self.y, self.z + 1): Direction.UP,
                }
    def above_the_table(self):
        return self.z >= 0

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Point(self.x - o.x, self.y - o.y, self.z - o.z)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z

    def __ne__(self, o):
        return not self == o

    def __hash__(self):
        return 1

    @staticmethod
    def left():
        return Point(-1, 0, 0)

    @staticmethod
    def right():
        return Point(1, 0, 0)

    @staticmethod
    def backward():
        return Point(0, -1, 0)

    @staticmethod
    def forward():
        return Point(0, 1, 0)

    @staticmethod
    def down():
        return Point(0, 0, -1)

    @staticmethod
    def up():
        return Point(0, 0, 1)

    @staticmethod
    def direction(direction: Direction):
        if direction == Direction.LEFT:
            return Point.left()
        if direction == Direction.RIGHT:
            return Point.right()
        if direction == Direction.BACKWARD:
            return Point.backward()
        if direction == Direction.FORWARD:
            return Point.forward()
        if direction == Direction.DOWN:
            return Point.down()
        if direction == Direction.UP:
            return Point.up()
