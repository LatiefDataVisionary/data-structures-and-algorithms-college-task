import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
from datetime import datetime
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

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("800x600")

        # Load background image
        self.background_image = Image.open("kampus-teknologi-yogya.jpg")
        self.background_image = self.background_image.resize((800, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.tasks = TaskList()

        self.create_widgets()
        self.task_notifications()
        
    def create_widgets(self):
        title_label = tk.Label(self.root, text="To-Do List App", font=("Arial", 24), bg='#4B8BBE', fg='white')
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.root, bg='#282C34')
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Judul:", bg='#282C34', fg='white').grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(form_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Deskripsi:", bg='#282C34', fg='white').grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(form_frame)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Kategori:", bg='#282C34', fg='white').grid(row=2, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Prioritas:", bg='#282C34', fg='white').grid(row=3, column=0, padx=5, pady=5)
        self.priority_entry = tk.Entry(form_frame)
        self.priority_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Deadline (YYYY-MM-DD HH:MM):", bg='#282C34', fg='white').grid(row=4, column=0, padx=5, pady=5)
        self.deadline_entry = tk.Entry(form_frame)
        self.deadline_entry.grid(row=4, column=1, padx=5, pady=5)

        add_button = tk.Button(form_frame, text="Tambah Tugas", command=self.add_task, bg='#61AFEF', fg='white')
        add_button.grid(row=5, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Judul", "Deskripsi", "Kategori", "Prioritas", "Deadline", "Status"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.heading("Prioritas", text="Prioritas")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=20)

        self.tree["style"] = "Custom.Treeview"
        self.root.tk.call("ttk::style", "layout", "Custom.Treeview", ["Treeview.treearea", {"sticky": "nswe"}])
        self.root.tk.call("ttk::style", "configure", "Custom.Treeview", "#D9D9D9", "black")

        button_frame = tk.Frame(self.root, bg='#282C34')
        button_frame.pack(pady=10)

        view_button = tk.Button(button_frame, text="Lihat Tugas", command=self.view_tasks, bg='#98C379', fg='black')
        view_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(button_frame, text="Tandai Selesai", command=self.complete_task, bg='#98C379', fg='black')
        complete_button.grid(row=0, column=1, padx=5)

        edit_button = tk.Button(button_frame, text="Edit Tugas", command=self.edit_task, bg='#98C379', fg='black')
        edit_button.grid(row=0, column=2, padx=5)

        delete_button = tk.Button(button_frame, text="Hapus Tugas", command=self.delete_task, bg='#98C379', fg='black')
        delete_button.grid(row=0, column=3, padx=5)

        search_frame = tk.Frame(self.root, bg='#282C34')
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Cari:", bg='#282C34', fg='white').grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5)
        search_button = tk.Button(search_frame, text="Cari", command=self.search_tasks, bg='#E5C07B', fg='black')
        search_button.grid(row=0, column=2, padx=5)

        tk.Label(search_frame, text="Kategori:", bg='#282C34', fg='white').grid(row=1, column=0, padx=5)
        self.category_filter_entry = tk.Entry(search_frame)
        self.category_filter_entry.grid(row=1, column=1, padx=5)
        filter_button = tk.Button(search_frame, text="Filter", command=self.filter_tasks, bg='#E5C07B', fg='black')
        filter_button.grid(row=1, column=2, padx=5)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_entry.get()
        deadline_str = self.deadline_entry.get()

        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal tidak valid. Gunakan format YYYY-MM-DD HH:MM")
            return

        task = Task(title, description, category, priority, deadline)
        self.tasks.add_task(task)
        self.view_tasks()

    def view_tasks(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks.get_tasks():
            self.tree.insert("", "end", values=(task.title, task.description, task.category, task.priority, task.deadline, task.status))

    def complete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_values = self.tree.item(selected_item[0], "values")
            tasks = self.tasks.get_tasks()
            for task in tasks:
                if (task.title, task.description, task.category, task.priority, str(task.deadline), task.status) == task_values:
                    task.status = "selesai"
                    break
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin ditandai selesai.")

    def edit_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_values = self.tree.item(selected_item[0], "values")
            tasks = self.tasks.get_tasks()
            for task in tasks:
                if (task.title, task.description, task.category, task.priority, str(task.deadline), task.status) == task_values:
                    new_title = tk.simpledialog.askstring("Edit Judul", "Masukkan judul baru:", initialvalue=task.title)
                    new_description = tk.simpledialog.askstring("Edit Deskripsi", "Masukkan deskripsi baru:", initialvalue=task.description)
                    new_category = tk.simpledialog.askstring("Edit Kategori", "Masukkan kategori baru:", initialvalue=task.category)
                    new_priority = tk.simpledialog.askstring("Edit Prioritas", "Masukkan prioritas baru:", initialvalue=task.priority)
                    new_deadline_str = tk.simpledialog.askstring("Edit Deadline", "Masukkan deadline baru (YYYY-MM-DD HH:MM):", initialvalue=str(task.deadline))

                    try:
                        new_deadline = datetime.strptime(new_deadline_str, "%Y-%m-%d %H:%M")
                    except ValueError:
                        messagebox.showerror("Error", "Format tanggal tidak valid. Gunakan format YYYY-MM-DD HH:MM")
                        return

                    task.title = new_title if new_title else task.title
                    task.description = new_description if new_description else task.description
                    task.category = new_category if new_category else task.category
                    task.priority = new_priority if new_priority else task.priority
                    task.deadline = new_deadline
                    break
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin diedit.")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_values = self.tree.item(selected_item[0], "values")
            tasks = self.tasks.get_tasks()
            for task in tasks:
                if (task.title, task.description, task.category, task.priority, str(task.deadline), task.status) == task_values:
                    tasks.remove(task)
                    break
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin dihapus.")

    def search_tasks(self):
        search_term = self.search_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if search_term in task.title.lower() or search_term in task.description.lower()]
        
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in filtered_tasks:
            self.tree.insert("", "end", values=(task.title, task.description, task.category, task.priority, task.deadline, task.status))

    def filter_tasks(self):
        category = self.category_filter_entry.get().lower()
        filtered_tasks = [task for task in self.tasks.get_tasks() if category in task.category.lower()]

        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in filtered_tasks:
            self.tree.insert("", "end", values=(task.title, task.description, task.category, task.priority, task.deadline, task.status))

    def task_notifications(self):
        threading.Thread(target=self._task_notifications, daemon=True).start()

    def _task_notifications(self):
        while True:
            now = datetime.now()
            for task in self.tasks.get_tasks():
                if task.status == 'belum selesai' and (task.deadline - now).total_seconds() <= 86400:
                    messagebox.showwarning("Peringatan!", f"Tugas '{task.title}' mendekati batas waktu (kurang dari 24 jam).")
            time.sleep(3600)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
