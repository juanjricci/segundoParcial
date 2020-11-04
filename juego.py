class Juego():

    def __init__(self, piece='', valid=[
            '1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3'
            ], board={}):
        self.piece = piece
        self.valid = valid
        self.board = board

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, value):
        self._piece = value

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value
