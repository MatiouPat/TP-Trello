import tkinter as tk

from trello_app import TrelloApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TrelloApp(root)
    root.geometry("600x400")  # Set initial window size
    root.resizable(True, True)  # Allow resizing in both directions
    root.mainloop()