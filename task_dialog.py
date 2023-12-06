import tkinter as tk
from tkinter import simpledialog


class TaskDialog(simpledialog.Dialog):
    def __init__(self, parent, title="Task Dialog"):
        self.task_name = ""
        self.task_description = ""
        self.task_assigneur = ""
        self.task_assigne = ""
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Task Name:").grid(row=0, column=0)
        tk.Label(master, text="Description:").grid(row=1, column=0)
        tk.Label(master, text="Assigneur:").grid(row=2, column=0)
        tk.Label(master, text="Assigné:").grid(row=3, column=0)

        self.task_name_entry = tk.Entry(master)
        self.task_description_entry = tk.Entry(master)
        self.task_assigneur_entry = tk.Entry(master)
        self.task_assigne_entry = tk.Entry(master)

        self.task_name_entry.grid(row=0, column=1)
        self.task_description_entry.grid(row=1, column=1)
        self.task_assigneur_entry.grid(row=2, column=1)
        self.task_assigne_entry.grid(row=3, column=1)

        return self.task_name_entry

    def apply(self):
        self.task_name = self.task_name_entry.get()
        self.task_description = self.task_description_entry.get()
        self.task_assigneur = self.task_assigneur_entry.get()
        self.task_assigne = self.task_assigne_entry.get()
        self.result = (self.task_name, self.task_description, self.task_assigneur, self.task_assigne)