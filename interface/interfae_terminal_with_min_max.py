from model.board import Board
from model.color import Color
from model.player.human import Human
from model.player.min_max import MinMax


def main():
    board = Board()
    player_1 = MinMax(Color.RED)
    player_2 = MinMax(Color.BLUE)
    print("hellow world. \n Wecome to the cubo4 game.\n It's a two player game, it's begin now. Blue begin")
    current_player = player_2
    board.begin(player_1.color)
    while True:
        position = current_player.play(board)
        print("player " + str(current_player.color) + " play " + str(position))
        board.play(current_player.color, position)
        win = board.win(current_player.color, position)
        if win:
            print("player" + str(current_player) + "win")
            print(board)
            return
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1


if __name__ == "__main__":
    main()
