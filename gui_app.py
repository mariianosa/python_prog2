import tkinter as tk
from tkinter import messagebox, filedialog
from workerdb import WorkerDB


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Worker Database GUI")

        self.collection = WorkerDB()

        # Create GUI components
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text="Choose an option:")
        self.menu_label.grid(row=0, column=0, pady=10)

        self.choice_var = tk.StringVar()
        self.choice_entry = tk.Entry(self.menu_frame, textvariable=self.choice_var)
        self.choice_entry.grid(row=0, column=1, pady=10)

        self.submit_button = tk.Button(self.menu_frame, text="Submit", command=self.handle_choice)
        self.submit_button.grid(row=0, column=2, pady=10)

    def ask_for_file(self):
        file_path = filedialog.askopenfilename(title="Select File", filetypes=[("CSV files", "*.csv")])
        return file_path

    def handle_choice(self):
        choice = self.choice_var.get()
        if choice == "1":
            self.collection.add_worker()
            messagebox.showinfo("Success", "Worker added successfully!")
        elif choice == "2":
            id_num = int(input("Enter worker ID you want to be changed: "))
            self.collection.edit(id_num)
            messagebox.showinfo("Success", "Worker edited successfully!")
        elif choice == "3":
            id_num = int(input("Enter worker ID you want to be deleted: "))
            self.collection.delete(id_num)
            messagebox.showinfo("Success", "Worker deleted successfully!")
        elif choice == "4":
            self.collection.display()
        elif choice == "5":
            self.collection.write_to_file('result.csv')
            messagebox.showinfo("Success", "Data written to file successfully!")
        elif choice == "6":
            field = input("Enter the field by which the list will be sorted: ")
            self.collection.d_sorted(field)
            self.collection.display()
        elif choice == "7":
            field = input("Enter the field for search:")
            value = input(f"Enter the value to search for in {field}: ")
            self.collection.search(field, value)
        elif choice == "8":
            self.collection.create_department_diagram()

        elif choice == "9":
            self.collection.read_from_file(self.ask_for_file())
            messagebox.showinfo("Success", "Data read from file successfully!")
