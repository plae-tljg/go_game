import tkinter as tk
from tkinter import messagebox

class GoGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Go Game")
        self.window.geometry("600x600")
        self.player_turn = "Black"

        self.board = []
        for i in range(19):
            row = []
            for j in range(19):
                row.append(0)
            self.board.append(row)

        self.buttons = []
        for i in range(19):
            row = []
            for j in range(19):
                button = tk.Button(self.window, command=lambda x=i, y=j: self.click(x, y), height=2, width=4)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.grid(row=19, column=0, columnspan=19)

    def click(self, x, y):
        if self.board[x][y] == 0:
            if self.player_turn == "Black":
                self.buttons[x][y].config(bg="black")
                self.board[x][y] = 1
                self.player_turn = "White"
            else:
                self.buttons[x][y].config(bg="white")
                self.board[x][y] = 2
                self.player_turn = "Black"
        else:
            messagebox.showerror("Error", "Stone already placed here!")

    def reset(self):
        self.player_turn = "Black"
        for i in range(19):
            for j in range(19):
                self.buttons[i][j].config(bg="SystemButtonFace")
                self.board[i][j] = 0

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GoGame()
    game.run()