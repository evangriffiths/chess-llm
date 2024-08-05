import sys

import chess
import chess.svg
from PyQt5.QtCore import QTimer
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget


class ChessBoardViewer:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = ChessBoardWidget()

    def show(self, board: chess.Board, duration: int):
        self.widget.show_board(board=board)
        if duration:
            self.widget.close_after(duration)
        self.app.exec_()


class ChessBoardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.svg_widget = QSvgWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.svg_widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Chess Board")

    def show_board(self, board: chess.Board):
        move = board.peek()
        self.svg_widget.load(
            chess.svg.board(
                board,
                fill={move.from_square: "gray"},
            ).encode("utf-8")
        )
        self.show()

    def close_after(self, duration: float):
        seconds = int(duration * 1000)
        QTimer.singleShot(seconds, self.close)


class Board:
    def __init__(self) -> None:
        self.board = chess.Board()
        self.viewer = ChessBoardViewer()

    def push_move(self, move: str) -> None:
        self.board.push_san(move)

    def show(self, duration: float) -> None:
        self.viewer.show(board=self.board, duration=duration)
