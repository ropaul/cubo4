from enum import Enum


class Color(bytes, Enum):

    def __new__(cls, value, enemy):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.enemy = enemy
        return obj

    RED = (1, 2)
    BLUE = (2, 1)

    def get_enemy(self):
        return Color(self.enemy)

