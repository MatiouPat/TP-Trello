import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, name, description="", completed=False):
        self.name = name
        self.description = description
        self.completed = completed

class TrelloApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Trello Board")

        self.tasks_in_progress = []
        self.completed_tasks = []

        self.in_progress_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.in_progress_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.completed_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.completed_listbox.pack(side=tk.RIGHT, padx=10, pady=10)

        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.master, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.show_description_button = tk.Button(self.master, text="Show Description", command=self.show_description)
        self.show_description_button.pack(pady=5)

    def add_task(self):
        task_name = simpledialog.askstring("Input", "Enter task name:")
        if task_name:
            task_description = simpledialog.askstring("Input", "Enter task description:")
            task = Task(name=task_name, description=task_description)
            self.tasks_in_progress.append(task)
            self.update_task_listboxes()

    def complete_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress.pop(selected_task_index[0])
            task.completed = True
            self.completed_tasks.append(task)
            self.update_task_listboxes()

    def show_description(self):
        selected_task_index = self.in_progress_listbox.curselection() or self.completed_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]] if selected_task_index[0] < len(self.tasks_in_progress) else self.completed_tasks[selected_task_index[0] - len(self.tasks_in_progress)]
            if task.description:
                messagebox.showinfo("Task Description", task.description)
            else:
                messagebox.showinfo("Task Description", "No description available.")

    def update_task_listboxes(self):
        self.in_progress_listbox.delete(0, tk.END)
        for task in self.tasks_in_progress:
            self.in_progress_listbox.insert(tk.END, task.name)

        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task.name)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrelloApp(root)
    root.mainloop()