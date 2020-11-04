from tateti import TaTeTi
from juego import Juego
from repositorios import Repositorios


if __name__ == '__main__':
    game = TaTeTi()
    juego = Juego()
    repo = Repositorios()

    print(game.board)
