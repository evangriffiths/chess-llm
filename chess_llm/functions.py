import chess
import chess.svg
from typing_extensions import Annotated

from chess_llm.board import Board

# Keep track of whether a move has been made.
made_move = False


def check_made_move(msg):
    board = Board()
    return board.check_made_move()


def get_legal_moves() -> Annotated[str, "A list of legal moves in UCI format"]:
    board = Board()
    return "Possible moves are: " + ",".join(
        [str(move) for move in board.board.legal_moves]
    )


def make_move(
    move: Annotated[str, "A move in UCI format."]
) -> Annotated[str, "Result of the move."]:
    print("make move entered")
    board = Board()
    move = chess.Move.from_uci(move)
    board.board.push_uci(str(move))
    board.made_move = True
    print(board.board)
    # # Display the board.
    # display(
    #     chess.svg.board(
    #         board,
    #         arrows=[(move.from_square, move.to_square)],
    #         fill={move.from_square: "gray"},
    #         size=200,
    #     )
    # )
    # Get the piece name.
    piece = board.board.piece_at(move.to_square)
    piece_symbol = piece.unicode_symbol()
    piece_name = (
        chess.piece_name(piece.piece_type).capitalize()
        if piece_symbol.isupper()
        else chess.piece_name(piece.piece_type)
    )
    return f"Moved {piece_name} ({piece_symbol}) from {chess.SQUARE_NAMES[move.from_square]} to {chess.SQUARE_NAMES[move.to_square]}."
