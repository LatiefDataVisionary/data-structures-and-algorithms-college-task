import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
from datetime import datetime
from tkcalendar import Calendar
import time
import threading

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
        self.root.geometry("800x600")

        # Load background image
        self.background_image = Image.open("kampus-teknologi-yogya.jpg")
        self.background_image = self.background_image.resize((1200, 900), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.tasks = TaskList()

        self.create_widgets()
        self.task_notifications()

    def create_widgets(self):
        style = ttk.Style()

        # Configure the style for the Treeview
        style.configure("Custom.Treeview", 
                        background="#333333",
                        foreground="white",
                        fieldbackground="#333333",
                        font=('Arial', 12))
        style.map("Custom.Treeview",
                  background=[("selected", "#4B8BBE")])
        
        # Configure the style for the Treeview headings
        style.configure("Custom.Treeview.Heading", 
                        background="#282C34",
                        foreground="white",
                        font=('Arial', 14, 'bold'))

        title_label = tk.Label(self.root, text="To-Do List App", font=("Arial", 24, "bold"), bg='#4B8BBE', fg='white')
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.root, bg='#282C34', bd=10, relief="ridge")
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

        self.tree = ttk.Treeview(self.root, columns=("Judul", "Deskripsi", "Kategori", "Prioritas", "Deadline", "Status"), show="headings", style="Custom.Treeview")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.heading("Prioritas", text="Prioritas")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        self.tree.tag_configure('belum_selesai', background='lightgray')
        self.tree.tag_configure('selesai', background='lightgreen')

        button_frame = tk.Frame(self.root, bg='#282C34')
        button_frame.pack(pady=10)

        complete_button = tk.Button(button_frame, text="Tandai Selesai", command=self.complete_task, bg='#98C379', fg='black', font=('Arial', 12))
        complete_button.grid(row=0, column=0, padx=5)

        edit_button = tk.Button(button_frame, text="Edit Tugas", command=self.edit_task, bg='#98C379', fg='black', font=('Arial', 12))
        edit_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Hapus Tugas", command=self.delete_task, bg='#98C379', fg='black', font=('Arial', 12))
        delete_button.grid(row=0, column=2, padx=5)

        search_frame = tk.Frame(self.root, bg='#282C34')
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
        self.status_filter_combobox = ttk.Combobox(search_frame, values=["Semua", "Belum Selesai", "Selesai"], font=('Arial', 12))
        self.status_filter_combobox.grid(row=2, column=1, padx=5)
        self.status_filter_combobox.current(0)
        status_filter_button = tk.Button(search_frame, text="Filter", command=self.filter_tasks, bg='#E5C07B', fg='black', font=('Arial', 12))
        status_filter_button.grid(row=2, column=2, padx=5)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_combobox.get()
        
        # Combine date and time from calendar and spinboxes
        deadline_date = self.deadline_entry.get_date()
        deadline_time = f"{self.hour_spinbox.get()}:{self.minute_spinbox.get()}"
        deadline_str = f"{deadline_date} {deadline_time}"
        
        try:
            deadline = datetime.strptime(deadline_str, "%m/%d/%y %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal atau waktu tidak valid.")
            return

        if not title or not description or not category:
            messagebox.showerror("Error", "Semua kolom harus diisi.")
            return

        task = Task(title, description, category, priority, deadline)
        self.tasks.add_task(task)
        self.update_task_list()

    def update_task_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for task in self.tasks.get_tasks():
            tags = ('selesai',) if task.status == 'selesai' else ('belum_selesai',)
            self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline.strftime("%Y-%m-%d %H:%M"), task.status), tags=tags)

    def complete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Pilih tugas terlebih dahulu.")
            return

        item = self.tree.item(selected_item)
        task_values = item['values']
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1] and task.category == task_values[2]:
                task.status = 'selesai'
                break
        self.update_task_list()

    def edit_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Pilih tugas terlebih dahulu.")
            return

        item = self.tree.item(selected_item)
        task_values = item['values']
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1] and task.category == task_values[2]:
                task.title = simpledialog.askstring("Edit Judul", "Edit Judul:", initialvalue=task.title)
                task.description = simpledialog.askstring("Edit Deskripsi", "Edit Deskripsi:", initialvalue=task.description)
                task.category = simpledialog.askstring("Edit Kategori", "Edit Kategori:", initialvalue=task.category)
                task.priority = simpledialog.askstring("Edit Prioritas", "Edit Prioritas:", initialvalue=task.priority)
                deadline_str = simpledialog.askstring("Edit Deadline", "Edit Deadline (YYYY-MM-DD HH:MM):", initialvalue=task.deadline.strftime("%Y-%m-%d %H:%M"))
                try:
                    task.deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    messagebox.showerror("Error", "Format tanggal atau waktu tidak valid.")
                    return
                break
        self.update_task_list()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Pilih tugas terlebih dahulu.")
            return

        item = self.tree.item(selected_item)
        task_values = item['values']
        for task in self.tasks.get_tasks():
            if task.title == task_values[0] and task.description == task_values[1] and task.category == task_values[2]:
                self.tasks.remove_task(task)
                break
        self.update_task_list()

    def search_tasks(self):
        search_term = self.search_entry.get()
        for i in self.tree.get_children():
            self.tree.delete(i)

        for task in self.tasks.get_tasks():
            if search_term.lower() in task.title.lower() or search_term.lower() in task.description.lower():
                tags = ('selesai',) if task.status == 'selesai' else ('belum_selesai',)
                self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline.strftime("%Y-%m-%d %H:%M"), task.status), tags=tags)

    def filter_tasks(self):
        category_filter = self.category_filter_entry.get()
        status_filter = self.status_filter_combobox.get()

        for i in self.tree.get_children():
            self.tree.delete(i)

        for task in self.tasks.get_tasks():
            if (category_filter.lower() in task.category.lower() if category_filter else True) and \
               (task.status == status_filter.lower() if status_filter != "Semua" else True):
                tags = ('selesai',) if task.status == 'selesai' else ('belum_selesai',)
                self.tree.insert("", tk.END, values=(task.title, task.description, task.category, task.priority, task.deadline.strftime("%Y-%m-%d %H:%M"), task.status), tags=tags)

    def task_notifications(self):
        def check_deadlines():
            while True:
                now = datetime.now()
                for task in self.tasks.get_tasks():
                    if task.status == 'belum selesai' and task.deadline <= now:
                        messagebox.showwarning("Deadline Warning", f"Tugas '{task.title}' telah mencapai deadline.")
                        task.status = 'selesai'
                        self.update_task_list()
                time.sleep(60)

        threading.Thread(target=check_deadlines, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
