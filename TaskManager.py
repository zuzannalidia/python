import datetime
import Task
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print("Zadanie usunięte pomyślnie.")
                return
        print("Nie znaleziono zadania o podanej nazwie.")

    def get_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        return filtered_tasks

    def filter_tasks_by_due_date(self, due_date):
        filtered_tasks = [task for task in self.tasks if task.due_date == due_date]
        return filtered_tasks

    def filter_tasks_by_status(self, completed):
        filtered_tasks = [task for task in self.tasks if task.completed == completed]
        return filtered_tasks

    def save_tasks_to_file(self, file_name):
        with open(file_name+'.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name},{task.description},{task.priority},{task.due_date},{task.category},{task.added_date},{task.completed},{task.completed_date}\n")
        print("Zadania zapisane do pliku.")

    def load_tasks_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_data = line.strip().split(',')
                name, description, priority, due_date, category, added_date_str, completed, completed_date_str = task_data
                added_date = datetime.datetime.strptime(added_date_str, "%Y-%m-%d %H:%M:%S")
                completed = True if completed == "True" else False
                completed_date = None
                if completed_date_str:
                    completed_date = datetime.datetime.strptime(completed_date_str, "%Y-%m-%d %H:%M:%S")
                task = Task(name, description, priority, due_date, category, added_date, completed)
                task.completed_date = completed_date
                self.tasks.append(task)
        print("Zadania wczytane z pliku.")

    def generate_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.completed for task in self.tasks)
        percent_completed = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        priorities = [task.priority for task in self.tasks]
        most_common_priority = max(set(priorities), key=priorities.count) if priorities else None

        total_execution_time = 0
        completed_on_time = 0
        for task in self.tasks:
            if task.completed and task.completed_date:
                total_execution_time += (task.completed_date - task.added_date).total_seconds()
                if task.completed_date <= datetime.datetime.strptime(task.due_date, "%Y-%m-%d"):
                    completed_on_time += 1

        average_execution_time = total_execution_time / completed_tasks if completed_tasks > 0 else 0
        percent_completed_on_time = (completed_on_time / completed_tasks) * 100 if completed_tasks > 0 else 0

        print("=== Statystyki ===")
        print(f"Całkowita liczba zadań: {total_tasks}")
        print(f"Liczba zakończonych zadań: {completed_tasks}")
        print(f"Procentowe zakończenie zadań: {percent_completed:.2f}%")
        print(f"Najczęstszy priorytet: {most_common_priority}")
        print(f"Średni czas wykonania zadania: {average_execution_time:.2f} sekund")
        print(f"Procentowe zakończenie zadań na czas: {percent_completed_on_time:.2f}%")
