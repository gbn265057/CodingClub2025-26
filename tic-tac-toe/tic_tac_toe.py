import tkinter as tk

from display import TicTacToeDisplay

if __name__ == "__main__":
    n_players = int(input("How many players? "))
    root = tk.Tk()
    display = TicTacToeDisplay(n_players, root)
    tk.mainloop()
