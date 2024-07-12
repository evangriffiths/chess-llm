import chess


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Board(metaclass=SingletonMeta):
    board: chess.Board
    made_move: bool = False

    def __init__(self) -> None:
        self.board = chess.Board()

    def check_made_move(self) -> bool:
        if self.made_move:
            self.made_move = False
            return True
        else:
            return False

    def is_game_over(self) -> bool:
        is_over = self.board.is_game_over()
        print(f"check if game over {is_over}")
        return is_over
