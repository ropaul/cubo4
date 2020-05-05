import sys
from copy import copy, deepcopy

from model.player.player import Player


class MinMax(Player):

    def __init__(self, color):
        Player.__init__(self, color)
        self.enemy = color.get_enemy()
        self.max_depth = 4

    def __init__(self, color, max_depth):
        Player.__init__(self, color)
        self.enemy = color.get_enemy()
        self.max_depth = max_depth

    def play(self, board):
        actions = board.get_playable_position()
        best_i = None
        best_val = -sys.maxsize

        for i, action in enumerate(actions):
            state = deepcopy(board)
            state.play(self.color, action)
            val = self.minimax(state, action, 0, False)

            if val > best_val:
                best_i = i
                best_val = val

        return actions[best_i]

    def minimax(self, state, action, depth, is_max):
        if state.win(self.color, action):
            return 10 - depth
        elif state.win(self.enemy, action):
            return -10 + depth
        # originaly, the game finish after each player have 21 turns
        elif depth >= self.max_depth:
            return 0

        actions = state.get_playable_position()

        if is_max:
            best = -sys.maxsize


            for action in actions:
                state_bis = deepcopy(state)
                state.play(self.color, action)
                val = self.minimax(state_bis, action, depth + 1, False)
                best = max(best, val)
        else:
            best = sys.maxsize

            for action in actions:
                state_bis = deepcopy(state)
                state.play(self.enemy, action)
                val = self.minimax(state_bis, action, depth + 1, True)
                best = min(best, val)

        return best