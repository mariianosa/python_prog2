class Worker:
    def __init__(self, worker_id="", name="", surname="", department="", salary=""):
        self._ID = int(worker_id) if worker_id else 0
        self.name = str(name)
        self.surname = str(surname)
        self.department = str(department)
        self.salary = float(salary) if salary else 0

    @staticmethod
    def validate_alpha(data, error_message, current_value=""):
        while True:
            try:
                value = input(data).strip() if not current_value else current_value
                if value.isalpha():
                    return value
                else:
                    raise ValueError(error_message)
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_float(data, error_message, current_value=""):
        if isinstance(current_value, float):
            return current_value

        while True:
            try:
                value = input(data).strip() if not current_value else current_value
                float_value = float(value)
                return float_value
            except ValueError:
                print(f"Error: {error_message}")
                break


    def read_worker(self):
        try:
            self._ID = int(input("ID:"))  # Валідація для ID
            self.name = self.validate_alpha("Name:")  # Валідація для імені
            self.surname = self.validate_alpha("Surname:")  # Валідація для прізвища
            self.department = self.validate_alpha("Department:")  # Валідація для відділу
            self.salary = float(input("Salary:"))  # Валідація для зарплати
        except ValueError as e:
            print(e)

    def display_worker(self):
        print("ID:", self._ID, "\n", "Name:", self.name, "\n", "Surname:", self.surname, "\n", "Department:",
              self.department, "\n", "Salary: ", self.salary)

    def get_id(self):
        return self._ID
