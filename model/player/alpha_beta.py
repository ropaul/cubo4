import sys
from copy import copy, deepcopy

from model.player.player import Player


class AlphaBeta(Player):

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
            val = self.alphabeta(state, action, 0, False, -sys.maxsize, sys.maxsize)

            if val > best_val:
                best_i = i
                best_val = val

        return actions[best_i]

    def alphabeta(self, state, action, depth, is_max, max_value, min_value):
        # print(depth, action, max_value, min_value)
        if state.win(self.color, action):
            return 21 - depth
        elif state.win(self.enemy, action):
            return -21 + depth
        # originaly, the game finish after each player have 21 turns
        elif depth >= self.max_depth:
            return 0

        actions = state.get_playable_position()

        if is_max:
            best = max_value


            for action in actions:
                state_bis = deepcopy(state)
                state.play(self.color, action)
                val = self.alphabeta(state_bis, action, depth + 1, False, best, min_value)
                best = max(best, val)
                if best > min_value:
                    return min_value
        else:
            best = min_value

            for action in actions:
                state_bis = deepcopy(state)
                state.play(self.enemy, action)
                val = self.alphabeta(state_bis, action, depth + 1, True, max_value, best)
                best = min(best, val)
                if best < max_value:
                    return max_value

        return best