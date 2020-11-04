from juego import Juego
from repositorios import Repositorios


class TaTeTi():
    juego = Juego()
    repo = Repositorios()

    valid = juego.valid
    board = repo.board
    piece = juego.piece

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner

    def __str__(self):
        expected = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        expected += '---+---+---\n3.1|3.2|3.3'
        return expected

    def input_position(self):
        while self.valid:
            posicion = input()
            if posicion in self.valid:
                self.valid.remove(posicion)
                return posicion
            else:
                pass

    def win(self):
        board = self.board
        for i in board:
            if board['1.1'] == ' x ' and board['2.2'] == ' x ' and board['3.3'] == ' x ':
                return True
            elif board['1.1'] == ' x ' and board['2.1'] == ' x ' and board['3.1'] == ' x ':
                return True
            elif board['1.2'] == ' o ' and board['2.2'] == ' o ' and board['3.2'] == ' o ':
                return True
            elif board['3.1'] == ' x ' and board['2.2'] == ' x ' and board['1.3'] == ' x ':
                return True
            elif board['1.1'] == ' o ' and board['1.2'] == ' o ' and board['1.3'] == ' o ':
                return True
            elif board['2.1'] == ' x ' and board['2.2'] == ' x ' and board['2.3'] == ' x ':
                return True
            else:
                return False


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
