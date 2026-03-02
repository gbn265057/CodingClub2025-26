import time
import tkinter as tk

from board import Player, TicTacToeBoard
from computer import TicTacToeVsComputer

class TicTacToeSquare(tk.Button):
    def __init__(self, display, row, column, *args, **kwargs):
        self.text = tk.StringVar()
        self.text.set("")
        self.display = display
        self.row = row
        self.column = column
        super().__init__(*args, command=self.on_click, textvariable=self.text, **kwargs)

    def on_click(self):
        self.display.click(self.row, self.column)

class TicTacToeDisplay(tk.Frame):
    def __init__(self, n_players, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_players = n_players
        if n_players == 2:
            self.board = TicTacToeBoard()
        else:
            self.board = TicTacToeVsComputer(Player.O)
        self.squares = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for column in range(3):
                square = TicTacToeSquare(self, row, column)
                square.grid(column=column, row=row)
                square.config(width=5, height=5)
                self.squares[row][column] = square

    def set_square_texts(self):
        for row_number, row in enumerate(self.squares):
            for column_number, square in enumerate(row):
                square_value = self.board.board[row_number][column_number]
                if square_value is not None:
                    square.text.set(square_value)

    def click(self, row, column):
        if self.board.play_at(row, column):
            self.set_square_texts()
            if self.board.winner is not None or self.board.is_full():
                self.update()
                time.sleep(0.5)
                self.clear()

    def clear(self):
        self.board.clear()

        for row in self.squares:
            for square in row:
                square.text.set("")
