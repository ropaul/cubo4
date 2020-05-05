from enum import Enum, unique


@unique
class Direction(bytes, Enum):

    def __new__(cls, value, inverse):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.inverse = inverse
        return obj

    UP = (1, 2)
    DOWN = (2, 1)
    FORWARD = (3, 4)
    BACKWARD = (4, 3)
    LEFT = (5, 6)
    RIGHT = (6, 5)

    def get_inverse(self):
        return Direction(self.inverse)

    def __str__(self):
        return self.name
