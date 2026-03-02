from itertools import chain, product
from random import choice

from board import Player, TicTacToeBoard


class TicTacToeVsComputer(TicTacToeBoard):
    def __init__(self, computer_player):
        super().__init__()
        self.non_losing_moves = {}
        for board_setup in product((None, Player.X, Player.O), repeat=9):
            self.non_losing_moves[tuple(board_setup)] = [
                (row, col) for row in range(3) for col in range(3)
            ]
        self.computer_player = computer_player
        if computer_player == Player.X:
            self.computer_move()

    def computer_move(self):
        board_setup = tuple(chain(*self.board))
        while True:
            if not self.non_losing_moves.get(board_setup, None):
                self.winner = self.computer_player.other_player()
                del self.non_losing_moves[board_setup]
                return None
            move = choice(self.non_losing_moves[board_setup])
            if super().play_at(move[0], move[1]):
                return move
            else:
                self.non_losing_moves[board_setup].remove(move)

    def play_at(self, row, column):
        last_board_state = tuple(chain(*self.board))
        played = super().play_at(row, column)
        if played:
            move = self.computer_move()
            if move is None or self.winner:
                self.non_losing_moves[last_board_state].remove(self.last_move)
            self.last_move = move
            self.last_board_state = last_board_state
        return played

    def clear(self):
        super().__init__()
