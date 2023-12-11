import csv
from worker import Worker
import pandas as pd
import matplotlib.pyplot as plt

class WorkerDB:
    def __init__(self):
        self.collection = []
        self.worker = Worker()

    def create_department_diagram(self):
        departments = [worker.department for worker in self.collection]
        data = {"Department": departments}
        df = pd.DataFrame(data)

        department_counts = df["Department"].value_counts()

        plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%')
        plt.title('Distribution of Workers by Department')
        plt.show()


    def generate_id(self):
        max_id = max([i.get_id() for i in self.collection], default=0)
        new_id = max_id + 1
        while True:
            yield new_id
            new_id += 1

    def read_from_file(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                try:
                    worker_id, name, surname, department, salary = row
                    worker = Worker(worker_id, name, surname, department, salary)
                    self.collection.append(worker)
                except (ValueError, IndexError) as e:
                    print(f"Error reading a line from the file: {e}")

    def add_worker(self):
        name = self.worker.validate_alpha("Enter name: ", "Error: Name should contain only letters.")
        surname = self.worker.validate_alpha("Enter surname: ", "Error: Surname should contain only letters.")
        department = self.worker.validate_alpha("Enter department: ", "Error: Department should contain only letters.")

        while True:
            try:
                salary_str = input("Enter salary: ")
                salary = float(salary_str)
                break
            except ValueError:
                print("Invalid input for salary. Please enter a valid number.")

        new_id = next(self.generate_id())

        worker = Worker(worker_id=new_id, name=name, surname=surname, department=department, salary=salary)
        self.collection.append(worker)


    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["id", "name", "surname", "department", "salary"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for i in self.collection:
                writer.writerow({"id": i.get_id(), "name": i.name, "surname": i.surname,
                                 "department": i.department, "salary": i.salary})

    def edit(self, id):
        for el in self.collection:
            if el.get_id() == id:
                print("1 - edit name\n",
                      "2 - edit surname\n", 
                      "3 - edit department\n", 
                      "4 - edit salary",
                      "\n")
                choice = int(input("enter your choice: "))
                if choice == 1:
                    n_name = input("enter new name: ")
                    el.name = n_name
                elif choice == 2:
                    n_surname = input("enter new surname: ")
                    el.surname = n_surname
                elif choice == 3:
                    n_department = input("enter new department: ")
                    el.department = n_department
                elif choice == 4:
                    n_salary =  input("enter new salary: ")
                    el.salary = n_salary

    def delete(self, id):
        for el in self.collection:
            if el.get_id() == id:
                self.collection.remove(el)

    def display(self):
        for el in self.collection:
            el.display_worker()

    def sort_decorator(sort_func):
        def wrapper(*args, **kwargs):
            key, field = args
            print("Sorted by ", field, " : ")
            sort_func(*args, **kwargs)    
        return wrapper

    
    @sort_decorator
    def d_sorted(self, field):
        getters = {
            "ID": lambda el: el._ID,
            "Name": lambda el: el.name.strip(),
            "Surname": lambda el: el.surname.strip(),
            "Depart": lambda el: el.department.strip(),
            "Salary": lambda el: el.salary.strip(),
         }
        getter = getters.get(field)

        if getter is not None:
            self.collection.sort(key = getter)
            return

        print("Invalid field for sorting")

    def search_decorator(search_func):
        def wrapper(*args, **kwargs):
            field = args[0]
            print("Search by", field, ":")
            search_func(*args, **kwargs)
        return wrapper
    

    @search_decorator
    def search(self, field, value):
        getters = {
            "ID": lambda el: el._ID,
            "Name": lambda el: el.name.strip(),
            "Surname": lambda el: el.surname.strip(),
            "Depart": lambda el: el.department.strip(),
            "Salary": lambda el: el.salary.strip(),
        }
        getter = getters.get(field)

        if getter is not None:
            found_workers = [
                el for el in self.collection
                if str(getter(el)).lower() == str(value).lower()
            ]
            if found_workers:
                for result in found_workers:
                    result.display_worker()
            else:
                print("No matching records found.")
        else:
            print("Invalid field for search")
