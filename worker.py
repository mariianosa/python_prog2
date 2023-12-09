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
    