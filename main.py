import tkinter as tk

from trello_app import TrelloApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TrelloApp(root)
    root.mainloop()