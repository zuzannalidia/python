import datetime

from pythonProject.Task import Task
from pythonProject.TaskManager import TaskManager


def main():
    task_manager = TaskManager()
    while True:
        print("\n===== Task Manager =====")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Edytuj zadanie")
        print("4. Oznacz zadanie jako zakończone")
        print("5. Wyświetl listę zadań")
        print("6. Filtrowanie zadań")
        print("7. Wygeneruj statystyki")
        print("8. Zapisz zadania do pliku")
        print("9. Wczytaj zadania z pliku")
        print("10. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Nazwa zadania: ")
            description = input("Opis zadania: ")
            priority = input("Priorytet (niski/średni/wysoki): ")
            # due_date = input("Termin wykonania (YYYY-MM-DD): ")
            #kacper dodal
            try:
                due_date = input("Termin wykonania (YYYY-MM-DD): ")
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Niepoprawny format daty. Użyj formatu YYYY-MM-DD.")
                exit()
            category = input("Kategoria (praca/osobiste/etc.): ")
            task = Task(name, description, priority, due_date, category)
            task_manager.add_task(task)
            print("Zadanie dodane pomyślnie.")
        elif choice == "2":
            name = input("Nazwa zadania do usunięcia: ")
            task_manager.remove_task(name)
        elif choice == "3":
            name = input("Nazwa zadania do edycji: ")
            task = task_manager.get_task(name)
            if task:
                print("Aktualne szczegóły zadania:")
                print(task)
                print("Podaj nowe dane (jeśli nie chcesz zmieniać danej, pozostaw puste):")
                new_name = input("Nowa nazwa zadania: ")
                new_description = input("Nowy opis zadania: ")
                new_priority = input("Nowy priorytet (niski/średni/wysoki): ")
                new_due_date = input("Nowy termin wykonania (YYYY-MM-DD): ")
                new_category = input("Nowa kategoria (praca/osobiste/etc.): ")
                task.update_task(name=new_name, description=new_description, priority=new_priority, due_date=new_due_date, category=new_category)
                print("Zadanie zaktualizowane pomyślnie.")
            else:
                print("Nie znaleziono zadania o podanej nazwie.")
        elif choice == "4":
            name = input("Nazwa zadania do oznaczenia jako zakończone: ")
            task = task_manager.get_task(name)
            if task:
                task.mark_as_completed()
            else:
                print("Nie znaleziono zadania o podanej nazwie.")
        elif choice == "5":
            task_manager.list_tasks()
        elif choice == "6":
            print("1. Filtrowanie po priorytecie")
            print("2. Filtrowanie po terminie wykonania")
            print("3. Filtrowanie po statusie (zakończone/niezakończone)")
            filter_choice = input("Wybierz opcję filtrowania: ")
            if filter_choice == "1":
                priority = input("Priorytet do filtrowania (niski/średni/wysoki): ")
                filtered_tasks = task_manager.filter_tasks_by_priority(priority)
            elif filter_choice == "2":
                due_date = input("Termin wykonania do filtrowania (YYYY-MM-DD): ")
                filtered_tasks = task_manager.filter_tasks_by_due_date(due_date)
            elif filter_choice == "3":
                status = input("Status do filtrowania (zakończone/niezakończone): ")
                completed = True if status.lower() == "zakończone" else False
                filtered_tasks = task_manager.filter_tasks_by_status(completed)
            else:
                print("Niepoprawny wybór.")
                continue
            print("=== Zadania po filtrowaniu ===")
            for task in filtered_tasks:
                print(task)
        elif choice == "7":
            task_manager.generate_statistics()
        elif choice == "8":
            file_name = input("Nazwa pliku do zapisu: ")
            task_manager.save_tasks_to_file(file_name)
        elif choice == "9":
            file_name = input("Nazwa pliku do wczytania: ")
            task_manager.load_tasks_from_file(file_name)
        elif choice == "10":
            print("Dziękujemy za skorzystanie z Task Managera!")
            break
        else:
            print("Niepoprawny wybór. Wybierz liczbę od 1 do 10.")

if __name__ == "__main__":
    main()