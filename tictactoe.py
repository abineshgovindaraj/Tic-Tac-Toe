import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.start_time = time.time()
        self.game_over = False

        self.turn_label = tk.Label(root, text="Turn: Player 1 (X)", font=("Arial", 14))
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_buttons()
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i+1, column=j)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.game_over = True
                end_time = time.time()
                duration = round(end_time - self.start_time, 2)
                winner = "Player 1 (X)" if self.current_player == "X" else "Player 2 (O)"
                messagebox.showinfo("Game Over", f"{winner} wins!\nTime: {duration} seconds")
                self.turn_label.config(text=f"{winner} won in {duration} sec")
            elif self.check_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                self.turn_label.config(text="It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(
                    text=f"Turn: {'Player 1 (X)' if self.current_player == 'X' else 'Player 2 (O)'}"
                )

    def check_winner(self, player):
        # Rows, columns and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.start_time = time.time()
        self.game_over = False
        self.turn_label.config(text="Turn: Player 1 (X)")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
