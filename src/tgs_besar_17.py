import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
from datetime import datetime
from tkcalendar import DateEntry  

class Task:
    def __init__(self, title, description, category, priority, deadline, status='belum selesai'):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.status = status
        self.deadline_entry = DateEntry(form_frame, font=('Arial', 12), selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task.title}, {task.description}, {task.category}, {task.priority}, {task.deadline}, {task.status}")

    def get_tasks(self):
        return self.tasks

    def remove_task(self, task):
        self.tasks.remove(task)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("900x700")
        self.tasks = TaskList()
        self.create_scrollable_canvas()
        self.create_widgets()
        self.task_notifications()

    def create_scrollable_canvas(self):
        self.canvas = tk.Canvas(self.root, bg='#282C34')
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#333333", foreground="white", fieldbackground="#333333", font=('Arial', 12))
        style.map("Custom.Treeview", background=[("selected", "#4B8BBE")])
        style.configure("Custom.Treeview.Heading", background="#282C34", foreground="black", font=('Arial', 14, 'bold'))

        title_label = tk.Label(self.scrollable_frame, text="To-Do List App", font=("Arial", 24, "bold"), bg='#4B8BBE', fg='white')
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.scrollable_frame, bg='#282C34', bd=10, relief="ridge")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Judul:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(form_frame, font=('Arial', 12))
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Deskripsi:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(form_frame, font=('Arial', 12))
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Kategori:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(form_frame, font=('Arial', 12))
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Prioritas:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5)
        self.priority_combobox = ttk.Combobox(form_frame, values=["Rendah", "Sedang", "Tinggi"], font=('Arial', 12))
        self.priority_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.priority_combobox.current(0)

        tk.Label(form_frame, text="Deadline:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=4, column=0, padx=5, pady=5)
        self.deadline_entry = Calendar(form_frame, font=('Arial', 12), selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        self.deadline_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Jam:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=4, column=2, padx=5, pady=5)
        self.hour_spinbox = tk.Spinbox(form_frame, from_=0, to=23, wrap=True, font=('Arial', 12), width=5, format="%02.0f")
        self.hour_spinbox.grid(row=4, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Menit:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=4, column=4, padx=5, pady=5)
        self.minute_spinbox = tk.Spinbox(form_frame, from_=0, to=59, wrap=True, font=('Arial', 12), width=5, format="%02.0f")
        self.minute_spinbox.grid(row=4, column=5, padx=5, pady=5)

        add_button = tk.Button(form_frame, text="Tambah Tugas", command=self.add_task, bg='#61AFEF', fg='white', font=('Arial', 12))
        add_button.grid(row=5, columnspan=6, pady=10)

        button_frame = tk.Frame(self.scrollable_frame, bg='#282C34')
        button_frame.pack(pady=10)

        complete_button = tk.Button(button_frame, text="Tandai Selesai", command=self.complete_task, bg='#98C379', fg='black', font=('Arial', 12))
        complete_button.grid(row=0, column=0, padx=5)

        edit_button = tk.Button(button_frame, text="Edit Tugas", command=self.edit_task, bg='#98C379', fg='black', font=('Arial', 12))
        edit_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Hapus Tugas", command=self.delete_task, bg='#98C379', fg='black', font=('Arial', 12))
        delete_button.grid(row=0, column=2, padx=5)

        tree_frame = tk.Frame(self.scrollable_frame)
        tree_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(tree_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(tree_frame, columns=("Judul", "Deskripsi", "Kategori", "Prioritas", "Deadline", "Status"), show="headings", style="Custom.Treeview", yscrollcommand=self.tree_scroll.set)
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        self.tree_scroll.config(command=self.tree.yview)

        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.heading("Prioritas", text="Prioritas")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")

        self.tree.tag_configure('belum_selesai', background='lightgray')
        self.tree.tag_configure('selesai', background='lightgreen')

        self.tree.bind("<Configure>", self.set_treeview_style)

        search_frame = tk.Frame(self.scrollable_frame, bg='#282C34')
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Cari:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, font=('Arial', 12))
        self.search_entry.grid(row=0, column=1, padx=5)
        search_button = tk.Button(search_frame, text="Cari", command=self.search_tasks, bg='#E5C07B', fg='black', font=('Arial', 12))
        search_button.grid(row=0, column=2, padx=5)

        tk.Label(search_frame, text="Kategori:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=1, column=0, padx=5)
        self.category_filter_entry = tk.Entry(search_frame, font=('Arial', 12))
        self.category_filter_entry.grid(row=1, column=1, padx=5)
        filter_button = tk.Button(search_frame, text="Filter", command=self.filter_tasks, bg='#E5C07B', fg='black', font=('Arial', 12))
        filter_button.grid(row=1, column=2, padx=5)

        tk.Label(search_frame, text="Status:", bg='#282C34', fg='white', font=('Arial', 12)).grid(row=2, column=0, padx=5)
        self.status_filter_combobox = ttk.Combobox(search_frame, values=["semua", "selesai", "belum selesai"], font=('Arial', 12))
        self.status_filter_combobox.grid(row=2, column=1, padx=5)
        self.status_filter_combobox.current(0)
        status_filter_button = tk.Button(search_frame, text="Filter", command=self.filter_by_status, bg='#E5C07B', fg='black', font=('Arial', 12))
        status_filter_button.grid(row=2, column=2, padx=5)

    def set_treeview_style(self, event):
        for col in self.tree["columns"]:
            self.tree.column(col, width=int(self.tree.winfo_width() / len(self.tree["columns"])))

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_combobox.get()
        deadline_date = self.deadline_entry.get_date().strftime("%d-%m-%Y")  # Ambil tanggal dari DateEntry
        hour = self.hour_spinbox.get()
        minute = self.minute_spinbox.get()
        deadline_time = f"{hour}:{minute}"

        if not all([title, description, category, priority, deadline_date, deadline_time]):
            messagebox.showerror("Error", "Semua field harus diisi.")
            return

        deadline = f"{deadline_date} {deadline_time}"
        task = Task(title, description, category, priority, deadline)
        self.tasks.add_task(task)
        self.display_tasks()

    def display_tasks(self):
        print("Displaying tasks...")
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task in self.tasks.get_tasks():
            print(f"Displaying task: {task.title}, {task.description}, {task.category}, {task.priority}, {task.deadline}, {task.status}")
            tag = 'selesai' if task.status == 'selesai' else 'belum_selesai'
            self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(tag,))

    def complete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Pilih tugas yang ingin ditandai sebagai selesai.")
            return
        task_values = self.tree.item(selected_item[0], "values")
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1]:
                task.status = 'selesai'
                break
        self.display_tasks()

    def edit_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Pilih tugas yang ingin di-edit.")
            return
        task_values = self.tree.item(selected_item[0], "values")
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1]:
                new_title = simpledialog.askstring("Edit Tugas", "Masukkan judul baru:", initialvalue=task.title)
                new_description = simpledialog.askstring("Edit Tugas", "Masukkan deskripsi baru:", initialvalue=task.description)
                new_category = simpledialog.askstring("Edit Tugas", "Masukkan kategori baru:", initialvalue=task.category)
                new_priority = simpledialog.askstring("Edit Tugas", "Masukkan prioritas baru:", initialvalue=task.priority)
                new_deadline = simpledialog.askstring("Edit Tugas", "Masukkan deadline baru (dd-mm-yyyy hh:mm):", initialvalue=task.deadline)

                if all([new_title, new_description, new_category, new_priority, new_deadline]):
                    task.title = new_title
                    task.description = new_description
                    task.category = new_category
                    task.priority = new_priority
                    task.deadline = new_deadline
                else:
                    messagebox.showerror("Error", "Semua field harus diisi.")
                break
        self.display_tasks()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Pilih tugas yang ingin dihapus.")
            return
        task_values = self.tree.item(selected_item[0], "values")
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1]:
                self.tasks.remove_task(task)
                break
        self.display_tasks()

    def search_tasks(self):
        search_query = self.search_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if search_query in task.title.lower()]
        self.display_filtered_tasks(filtered_tasks)

    def filter_tasks(self):
        category_filter = self.category_filter_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if category_filter in task.category.lower()]
        self.display_filtered_tasks(filtered_tasks)

    def filter_by_status(self):
        status_filter = self.status_filter_combobox.get()
        if status_filter == "semua":
            filtered_tasks = self.tasks.get_tasks()
        else:
            filtered_tasks = [task for task in self.tasks.get_tasks() if task.status == status_filter]
        self.display_filtered_tasks(filtered_tasks)

    def display_filtered_tasks(self, filtered_tasks):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task in filtered_tasks:
            tag = 'selesai' if task.status == 'selesai' else 'belum_selesai'
            self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(tag,))

    def task_notifications(self):
        now = datetime.now().strftime("%d-%m-%Y %H:%M")
        for task in self.tasks.get_tasks():
            if task.deadline == now and task.status != 'selesai':
                messagebox.showinfo("Pemberitahuan Tugas", f"Tugas '{task.title}' sudah mencapai deadline!")
        self.root.after(60000, self.task_notifications)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
