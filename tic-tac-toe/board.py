import enum


class Player(enum.StrEnum):
    X = "X"
    O = "O"

    def other_player(self):
        return self.O if self == self.X else self.X


class TicTacToeBoard:
    def __init__(self):
        self.current_player = Player.X
        self.board =[[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def in_bounds(self, row, column):
        return 0 <= row <= 2 and 0 <= column <= 2

    def play_at(self, row, column):
        if not self.in_bounds(row, column) or self.board[row][column] is not None:
            return False
        self.board[row][column] = self.current_player
        self.current_player = self.current_player.other_player()
        self.winner = self.check_winner()
        return True
    
    def check_winner(self):
        for row in self.board:
            if row[0] and len(set(row)) == 1:
                return row[0]
        for column_number in range(3):
            column = [row[column_number] for row in self.board]
            if column[0] and len(set(column)) == 1:
                return column[0]
        diagonal_one = (self.board[0][0], self.board[1][1], self.board[2][2])
        if diagonal_one[0] and len(set(diagonal_one)) == 1:
            return diagonal_one[0]
        diagonal_one = (self.board[2][0], self.board[1][1], self.board[0][2])
        if diagonal_one[0] and len(set(diagonal_one)) == 1:
            return diagonal_one[0]
        return None

    def is_full(self):
        return all(all(row) for row in self.board)

    def clear(self):
        self.__init__()
