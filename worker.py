import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch

id_count = 0

class Worker:
    def __init__(self, worker_id = "", name="", surname="", department="", salary=""):
        self._ID = int(worker_id)
        self.name = str(name)
        self.surname = str(surname)
        self.department = str(department)
        self.salary = float(salary)

    def is_alpha(self, data):
        try:
            value = input(data)
            if value.isalpha():
                return value
        except TypeError:
            print('ERROR. It needs to be letter')

    def read_worker(self):
        try:
            self._ID = input("ID: ")
            self.name = self.is_alpha("Name: ")
            self.surname = self.is_alpha("Surname: ")
            self.department = self.is_alpha("Department: ")
            self.salary = input("Salary: ")
        except ValueError as e:
            print(e)

    




    def display_worker(self):
        print("ID:", self._ID, "\n", "Name:", self.name, "\n", "Surname:", self.surname, "\n", "Department:",
              self.department, "\n","Salary: ",self.salary)

    def get_id(self):
         return self._ID 
    
    

class WorkerDB:
    def __init__(self):
        self.collection = []

    def read_from_file(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")  
            for row in reader:
                try:
                    worker_id, name, surname, department, salary = row[0], row[1], row[2], row[3], row[4]
                    worker = Worker(worker_id, name, surname, department, salary)
                    self.collection.append(worker)

                except ValueError as e:
                    print(e)



    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["id", "name", "surname", "department", "salary"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for i in self.collection:
                writer.writerow({"id": i.get_id(), "name": i.name, "surname": i.surname,
                                 "department": i.department, "salary": i.salary})

    def add_worker(self):

        name = input("Enter name: ")
        surname = input("Enter surname: ")
        department = input("Enter department: ")
        salary = input("Enter salary: ")

        max_id = max([int(w.get_id()) for w in self.collection], default=0)
        new_id = max_id + 1

        worker = Worker(worker_id=new_id, name=name, surname=surname, department=department, salary=salary)

        self.collection.append(worker)

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
            "Name": lambda el: el.name,
            "Surname": lambda el: el.surname,
            "Depart": lambda el: el.department,
            "Salary": lambda el: el.salary,
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
            "Name": lambda el: el.name,
            "Surname": lambda el: el.surname,
            "Depart": lambda el: el.department,
            "Salary": lambda el: el.salary,
        }
        getter = getters.get(field)

        if getter is not None:
            results = [
                el for el in self.collection 
                    if str(getter(el)) == str(value)]
            if results:
                for result in results:
                    result.display_worker()
            else:
                print("No matching records found.")
        else:
            print("Invalid field for search")

            
class TestWorkerAndWorkerDB(unittest.TestCase):
    def setUp(self):
        self.collection = WorkerDB()

    def test_add_worker(self):
        input_data = 'Max, Olefir, IT, 3000'
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.add_worker()
        self.assertEqual(len(self.collection.collection), 1)
        
    def test_delete_worker(self):
        example_worker = Worker(worker_id = "15", name="Anton", surname="Ivankiv", department="OLA", salary="8000")
        self.collection.collection.append(example_worker)
        input_data = "15"
        with patch('builtins.input', side_effect=input_data.split(',')):
            self.collection.delete(15)
        self.assertEqual(len(self.collection.collection), 0)
        
        

def main():
    filename = 'worker.csv'
    collection = WorkerDB()
    choice = input("Enter R to read from file: ")
    collection.read_from_file(filename)
    unittest.main(argv=[''], exit=False)
    
    while choice != '0':
        print("  1. Add worker\n",
                "2. Edit worker\n",
                "3. Delete worker\n",
                "4. Display list of workers\n", 
                "5. Write list to file\n", 
                "6. Sort by chosen field\n",
                "7. Search by chosen field\n",
                "8. Do diagram\n",
             	"9. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            collection.add_worker()
        elif choice == "2":
            id_num = int(input("Enter worker ID you want to be changed: "))
            collection.edit(id_num)
        elif choice == "3":
            id_num = int(input("Enter worker ID you want to be deleted: "))
            collection.delete(id_num)
        elif choice == "4":
            collection.display()
        elif choice == "5":
            collection.write_to_file('result.csv')
        elif choice == "6":
            field=input("Enter the field by which the list will be sorted: ")
            collection.d_sorted(field)
            collection.display()
        elif choice == "7":
            field = input("Enter the field for search:")
            value = input(f"Enter the value to search for in {field}: ")
            collection.search(field, value)
        elif choice == "8":
            departments = [worker.department for worker in collection.collection]
            unique_departments = list(set(departments))

            department_counts = [departments.count(dep) for dep in unique_departments]

            plt.bar(unique_departments, department_counts)
            plt.xlabel('Department')
            plt.ylabel('Number of Workers')
            plt.title('Number of Workers in Each Department')
            plt.show()

            
        elif choice == "9":
            choice = '0'

if __name__ == "__main__":
    main()