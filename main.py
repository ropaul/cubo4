from model import *
from model import color
from model.board import Board
from model.color import Color
from model.point import Point


def main():
    print("hello world!")
    board = Board()
    board.begin(Color.RED)
    print(board)
    for x in board.get_playable_position():
        print(x)
    # board.play(Color.BLUE, Point(0, 0, 1))
    # board.play(Color.BLUE, Point(0, 0, 2))
    # board.play(Color.BLUE, Point(0, 0, 3))
    # board.play(Color.BLUE, Point(0, 0, 4))
    # for x, y in board.cases.items():
    #     print("yann", x, y)
    # print(board.win(Color.BLUE, Point(0, 0, 4)))

if __name__ == "__main__":
    main()
