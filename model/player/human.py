from model.player.player import Player


class Human(Player):

    def play(self, board):
        print("player " + str(self.color) + " please, chose a position to play")
        positions = board.get_playable_position()
        for i in range(len(positions)):
            print("write " + str(i) + " for " + str(positions[i]))
        x = input()
        return positions[int(x)]
