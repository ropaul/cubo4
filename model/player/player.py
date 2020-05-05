import abc


class Player:

    def __init__(self, color):
        super()
        self.color = color

    @abc.abstractmethod
    def play(self, board):
        pass
