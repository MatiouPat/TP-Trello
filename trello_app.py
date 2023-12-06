import tkinter as tk
from tkinter import LEFT, simpledialog, messagebox

from task import Task
from task_dialog import TaskDialog

class TrelloApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Trello Board")

        self.center_window(1920, 1080)

        self.tasks_in_progress = []
        self.completed_tasks = []

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.TOP, pady=10)

        self.in_progress_listbox_frame = tk.Frame(self.master)
        self.in_progress_listbox_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.completed_listbox_frame = tk.Frame(self.master)
        self.completed_listbox_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.in_progress_listbox = tk.Listbox(self.in_progress_listbox_frame, selectmode=tk.SINGLE, bg="#E1F5FE")  # Light blue for in-progress tasks
        self.in_progress_listbox.pack()

        self.completed_listbox = tk.Listbox(self.completed_listbox_frame, selectmode=tk.SINGLE, bg="#C8E6C9")  # Light green for completed tasks
        self.completed_listbox.pack()

        tk.Label(self.in_progress_listbox_frame, text="A faire", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self.completed_listbox_frame, text="Réalisé", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="➕ New Task", command=self.add_task, bg="#4CAF50", fg="white")  # Green button
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.complete_task_button = tk.Button(self.button_frame, text="✅ Complete Task", command=self.complete_task, bg="#FFC107", fg="white")  # Amber button
        self.complete_task_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_task_button = tk.Button(self.button_frame, text="❌ Delete Task", command=self.delete_task, bg="#FF0000", fg="white")  # Red button
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        self.modify_task_button = tk.Button(self.button_frame, text="🖊️ Modify Task", command=self.modify_task, bg="#FF9800", fg="white")  # Orange button
        self.modify_task_button.pack(side=tk.LEFT, padx=5)

        self.show_description_button = tk.Button(self.button_frame, text="ℹ️ Show Description", command=self.show_description, bg="#1976D2", fg="white")  # Blue button
        self.show_description_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task_dialog = TaskDialog(self.master, title="Add Task")
        if task_dialog.result:
            task = Task(
                name=task_dialog.task_name,
                description=task_dialog.task_description,
                assigneur=task_dialog.task_assigneur,
                assigne=task_dialog.task_assigne
            )
            self.tasks_in_progress.append(task)
            self.update_task_listboxes()

    def center_window(self, width, height):
        # Obtenir la résolution de l'écran
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculer les coordonnées x et y pour centrer la fenêtre
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Définir la position de la fenêtre
        self.master.geometry("+{}+{}".format(x, y))

    def complete_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]]
            task.complete()
            self.completed_tasks.append(task)
            self.tasks_in_progress.remove(task)
            self.update_task_listboxes()

    def delete_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]]
            self.tasks_in_progress.remove(task)
            self.update_task_listboxes()

    def modify_task(self):
        selected_task_index = self.in_progress_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]]
            task_dialog = TaskDialog(self.master, title="Modify Task")
            if task_dialog.result:
                task.name = task_dialog.task_name
                task.description = task_dialog.task_description
                task.assigneur = task_dialog.task_assigneur
                task.assigne = task_dialog.task_assigne
                self.update_task_listboxes()

    def show_description(self):
        selected_task_index = self.in_progress_listbox.curselection() or self.completed_listbox.curselection()
        if selected_task_index:
            task = self.tasks_in_progress[selected_task_index[0]] if selected_task_index[0] < len(self.tasks_in_progress) else self.completed_tasks[selected_task_index[0] - len(self.tasks_in_progress)]
            if task.description:
                description = f"Description: {task.description}\n"
            else:
                description = "No description available.\n"

            assigneur = f"Assigneur: {task.assigneur}\n"
            assigne = f"Assigné: {task.assigne}\n"

            creation_date = f"Created on: {task.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"

            if task.completed:
                completion_date = f"Completed on: {task.completion_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            else:
                completion_date = ""

            messagebox.showinfo("Task Details", f"{description}{assigneur}{assigne}{creation_date}{completion_date}")

    def update_task_listboxes(self):
        self.in_progress_listbox.delete(0, tk.END)
        for task in self.tasks_in_progress:
            self.in_progress_listbox.insert(tk.END, task.name)

        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task.name)