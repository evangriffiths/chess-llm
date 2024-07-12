import chess

if __name__ == "__main__":
    print('start')
    board = chess.Board()
    print(board)
    #########
    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Qh5")
    board.push_san("Nc6")
    board.push_san("Bc4")
    board.push_san("Nf6")
    board.push_san("Qxf7")
    print(board.is_checkmate())
    #########
    print(board.move_stack)
    print('end')