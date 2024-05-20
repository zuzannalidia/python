import datetime

class Task:
    def __init__(self, name, description, priority, due_date, category, added_date=None, completed=False):
        self.name = name
        self.description = description
        self.priority = priority
        # self.due_date = due_date
        #to tez dodal kacper
        if due_date:
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
                self.due_date = due_date
            except ValueError:
                print("Niepoprawny format daty. Użyj formatu YYYY-MM-DD.")
                #kacper dodal
                exit()
        self.category = category
        self.added_date = added_date if added_date else datetime.datetime.now()
        self.completed = completed
        self.completed_date = None

    def mark_as_completed(self):
        if not self.completed:
            self.completed = True
            self.completed_date = datetime.datetime.now()
            print("Zadanie oznaczone jako zakończone.")
        else:
            print("To zadanie już jest oznaczone jako zakończone.")

    def update_task(self, name=None, description=None, priority=None, due_date=None, category=None):
        if self.completed:
            print("Nie można edytować zakończonego zadania.")
            return
        if name:
            self.name = name
        if description:
            self.description = description
        if priority:
            self.priority = priority
        if due_date:
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
                self.due_date = due_date
            except ValueError:
                print("Niepoprawny format daty. Użyj formatu YYYY-MM-DD.")
        if category:
            self.category = category


    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nPriority: {self.priority}\nDue Date: {self.due_date}\nCategory: {self.category}\nCompleted: {self.completed}"