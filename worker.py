import csv

id_count = 0

class Worker:
    def __init__(self, name="", surname="", department="", salary=""):
        global id_count
        id_count += 1
        self.__ID = id_count
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def read_worker(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")
        self.department = input("Department: ")
        self.salary = input("Salary: ")

    def display_worker(self):
        print("ID:", self.__ID, "\n", "Name:", self.name, "\n", "Surname:", self.surname, "\n", "Department:",
              self.department, "\n","Salary: ",self.salary)

    def get_id(self):
        return self.__ID

class WorkerDB:
    def __init__(self):
        self.collection = []

    def read_from_file(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=" ")  
            for row in reader:
                name, surname, department, salary = row[0], row[1], row[2], row[3]
                worker = Worker(name, surname, department, salary)
                self.collection.append(worker)



    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["id", "name", "surname", "department", "salary"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for i in self.collection:
                writer.writerow({"id": i.get_id(), "name": i.name, "surname": i.surname,
                                 "department": i.department, "salary": i.salary})

    def add(self):
        worker = Worker()
        worker.read_worker()
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

def main():
    filename = 'worker.csv'
    collection = WorkerDB()
    choice = input("Enter R to read from file: ")
    collection.read_from_file(filename)
    while choice != '0':
        print("  1. Add worker\n",
                "2. Edit worker\n",
                "3. Delete worker\n",
                "4. Display list of workers\n", 
                "5. Write list to file\n", 
                "6. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            collection.add()
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
            choice = '0'

if __name__ == "__main__":
    main()