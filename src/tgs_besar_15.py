import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
from datetime import datetime
from tkcalendar import Calendar


class Task:
    def __init__(self, title, description, category, priority, deadline, status='belum selesai'):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.status = status


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

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
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview, width=20)
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
        self.status_combobox = ttk.Combobox(search_frame, values=["Semua", "Selesai", "Belum Selesai"], font=('Arial', 12))
        self.status_combobox.grid(row=2, column=1, padx=5)
        self.status_combobox.current(0)
        status_button = tk.Button(search_frame, text="Filter Status", command=self.filter_status, bg='#E5C07B', fg='black', font=('Arial', 12))
        status_button.grid(row=2, column=2, padx=5)

    def set_treeview_style(self, event=None):
        self.tree.tk.call(self.tree, 'tag', 'configure', 'transparent', '-background', 'SystemWindow', '-foreground', 'SystemWindowText')

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_combobox.get()
        deadline_date = self.deadline_entry.get_date()
        deadline_hour = self.hour_spinbox.get()
        deadline_minute = self.minute_spinbox.get()
        deadline = f"{deadline_date} {deadline_hour}:{deadline_minute}"

        if title and description and category:
            new_task = Task(title, description, category, priority, deadline)
            self.tasks.add_task(new_task)
            self.refresh_task_list()
            self.clear_form()
        else:
            messagebox.showwarning("Peringatan", "Semua field harus diisi.")

    def complete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_index = self.tree.index(selected_item)
            task = self.tasks.get_tasks()[task_index]
            task.status = "selesai"
            self.refresh_task_list()

    def edit_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_index = self.tree.index(selected_item)
            task = self.tasks.get_tasks()[task_index]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, task.title)
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, task.description)
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, task.category)
            self.priority_combobox.set(task.priority)
            deadline_date, deadline_time = task.deadline.split(" ")
            self.deadline_entry.set_date(datetime.strptime(deadline_date, "%m/%d/%y"))
            deadline_hour, deadline_minute = deadline_time.split(":")
            self.hour_spinbox.delete(0, tk.END)
            self.hour_spinbox.insert(0, deadline_hour)
            self.minute_spinbox.delete(0, tk.END)
            self.minute_spinbox.insert(0, deadline_minute)
            self.tasks.remove_task(task)
            self.refresh_task_list()

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_index = self.tree.index(selected_item)
            task = self.tasks.get_tasks()[task_index]
            self.tasks.remove_task(task)
            self.refresh_task_list()

    def search_tasks(self):
        search_query = self.search_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if search_query in task.title.lower()]
        self.refresh_task_list(filtered_tasks)

    def filter_tasks(self):
        category_query = self.category_filter_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if category_query in task.category.lower()]
        self.refresh_task_list(filtered_tasks)

    def filter_status(self):
        status_query = self.status_combobox.get().lower()
        if status_query == "semua":
            self.refresh_task_list(self.tasks.get_tasks())
        else:
            filtered_tasks = [task for task in self.tasks.get_tasks() if task.status == status_query]
            self.refresh_task_list(filtered_tasks)

    def refresh_task_list(self, tasks=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if tasks is None:
            tasks = self.tasks.get_tasks()
        for task in tasks:
            tag = 'selesai' if task.status == 'selesai' else 'belum_selesai'
            self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(tag,))

    def clear_form(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.priority_combobox.current(0)
        self.deadline_entry.set_date(datetime.now())
        self.hour_spinbox.delete(0, tk.END)
        self.hour_spinbox.insert(0, "00")
        self.minute_spinbox.delete(0, tk.END)
        self.minute_spinbox.insert(0, "00")

    def task_notifications(self):
        now = datetime.now().strftime("%m/%d/%y %H:%M")
        for task in self.tasks.get_tasks():
            if task.deadline == now and task.status == 'belum selesai':
                messagebox.showinfo("Pengingat Tugas", f"Tugas '{task.title}' sudah mencapai deadline.")
        self.root.after(60000, self.task_notifications)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
