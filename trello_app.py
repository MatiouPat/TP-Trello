import tkinter as tk
from tkinter import simpledialog, messagebox

from task import Task

class TrelloApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Trello Board")

        self.tasks_in_progress = []
        self.completed_tasks = []

        self.in_progress_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="#E1F5FE")  # Light blue for in-progress tasks
        self.in_progress_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.completed_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="#C8E6C9")  # Light green for completed tasks
        self.completed_listbox.pack(side=tk.RIGHT, padx=10, pady=10)

        self.add_task_button = tk.Button(self.master, text="➕ New Task", command=self.add_task, bg="#4CAF50", fg="white")  # Green button
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.master, text="✅ Complete Task", command=self.complete_task, bg="#FFC107", fg="white")  # Amber button
        self.complete_task_button.pack(pady=5)

        self.modify_task_button = tk.Button(self.master, text="🖊️ Modify Task", command=self.modify_task, bg="#FF9800", fg="white")  # Orange button
        self.modify_task_button.pack(pady=5)

        self.show_description_button = tk.Button(self.master, text="ℹ️ Show Description", command=self.show_description, bg="#1976D2", fg="white")  # Blue button
        self.show_description_button.pack(pady=5)

    def on_add_task(self, task):
            self.tasks_in_progress.append(task)
            self.update_task_listboxes()

    def add_task(self):
        add_task_window = tk.Toplevel(self.master)
        add_task_window.title("Ajouter une nouvelle tache")

        #UI
        tk.Label(master=add_task_window, text="Nom").pack(pady=5)
        name = tk.Entry(master=add_task_window, width=24)
        name.pack(pady=5)
        tk.Label(master=add_task_window, text="Description").pack(pady=5)
        description = tk.Text(master=add_task_window, width=24)
        description.pack(pady=5)
        tk.Button(master=add_task_window, text="Annuler", height=1, foreground="#090D11", borderwidth=1, padx=4, pady=4, command=lambda: (add_task_window.destroy())).pack()
        tk.Button( master=add_task_window, text="Ajouter la tache", height=1, background='#D87D40', foreground="#FFFFFF", borderwidth=1, padx=4, pady=4, command=lambda: (self.on_add_task(Task(name=name.get(), description=description.get("1.0", tk.END))), add_task_window.destroy())).pack()

        
        """
        task_name = simpledialog.askstring("Input", "Enter task name:")
        task_description = simpledialog.askstring("Input", "Enter task description:")
        """

    def complete_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]]
            task.complete()
            self.completed_tasks.append(task)
            self.tasks_in_progress.remove(task)
            self.update_task_listboxes()

    def modify_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]]
            new_name = simpledialog.askstring("Input", "Enter new task name:", initialvalue=task.name)
            new_description = simpledialog.askstring("Input", "Enter new task description:", initialvalue=task.description)
            if new_name is not None:
                task.name = new_name
                task.description = new_description
                self.update_task_listboxes()

    def show_description(self):
        selected_task_index = self.in_progress_listbox.curselection() or self.completed_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]] if selected_task_index[0] < len(self.tasks_in_progress) else self.completed_tasks[selected_task_index[0] - len(self.tasks_in_progress)]
            if task.description:
                description = f"Description: {task.description}\n"
            else:
                description = "No description available.\n"

            creation_date = f"Created on: {task.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"

            if task.completed:
                completion_date = f"Completed on: {task.completion_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            else:
                completion_date = ""

            messagebox.showinfo("Task Details", f"{description}{creation_date}{completion_date}")

    def update_task_listboxes(self):
        self.in_progress_listbox.delete(0, tk.END)
        for task in self.tasks_in_progress:
            self.in_progress_listbox.insert(tk.END, task.name)

        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task.name)