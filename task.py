from datetime import datetime

class Task:
    def __init__(self, name, description="", assigneur="", assigne="", completed=False):
        self.name = name
        self.description = description
        self.assigneur = assigneur
        self.assigne = assigne
        self.completed = completed
        self.creation_date = datetime.now()
        self.completion_date = None

    def complete(self):
        self.completed = True
        self.completion_date = datetime.now()