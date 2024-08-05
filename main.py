from chess_llm.board import Board

if __name__ == "__main__":
    board = Board()
    moves = ["e4", "e5"]

    for move in moves:
        board.push_move(move)
        board.show(duration=0.5)
