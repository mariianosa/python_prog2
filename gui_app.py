import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from workerdb import WorkerDB

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Worker Database GUI")

        self.collection = WorkerDB()

        # Create GUI components
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        # Add buttons with corresponding functionality
        self.add_button("Add Worker", lambda: self.collection.add_worker(), messagebox.showinfo, "Success", "Worker added successfully!")
        self.add_button("Edit Worker", lambda: self.collection.edit(simpledialog.askinteger("Edit Worker", "Enter worker ID you want to be changed:")), 
                        messagebox.showinfo, "Success", "Worker edited successfully!")
        self.add_button("Delete Worker", lambda: self.collection.delete(simpledialog.askinteger("Delete Worker", "Enter worker ID you want to be deleted:")), 
                        messagebox.showinfo, "Success", "Worker deleted successfully!")
        self.add_button("Display Workers", self.collection.display)
        self.add_button("Write to File", lambda: self.collection.write_to_file('result.csv'), messagebox.showinfo, "Success", "Data written to file successfully!")
        self.add_button("Sort Workers", lambda: self.collection.d_sorted(simpledialog.askstring("Sort Workers", "Enter the field by which the list will be sorted:")), self.collection.display)
        self.add_button("Search Workers", self.search_worker)
        self.add_button("Department Diagram", self.collection.create_department_diagram)
        self.add_button("Read from File", lambda: self.collection.read_from_file(self.ask_for_file()), messagebox.showinfo, "Success", "Data read from file successfully!")

    def add_button(self, text, command, info_function=None, *info_args):
        def wrapped_command():
            command()
            if info_function:
                info_function(*info_args)

        btn = tk.Button(self.menu_frame, text=text, command=wrapped_command)
        btn.pack(pady=10)

    def ask_for_file(self):
        file_path = filedialog.askopenfilename(title="Select File", filetypes=[("CSV files", "*.csv")])
        return file_path
    def search_worker(self):
        field = simpledialog.askstring("Search Workers", "Enter the field for search:")
        value = simpledialog.askstring("Search Workers", f"Enter the value to search for in {field}:")
        self.collection.search(field, value)


# Використання класу
root = tk.Tk()
app = GUIApp(root)
root.mainloop()
