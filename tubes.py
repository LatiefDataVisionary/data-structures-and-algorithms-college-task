import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tkcalendar import DateEntry


class Task:
    def __init__(self, title, description, category, priority, deadline, status="belum selesai"):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.status = status


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, old_task, new_task):
        index = self.tasks.index(old_task)
        self.tasks[index] = new_task


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = TaskManager()

        # Frame for input fields
        self.input_frame = ttk.Frame(root, padding="10")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(self.input_frame, text="Judul:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = ttk.Entry(self.input_frame)
        self.title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.input_frame, text="Deskripsi:").grid(row=1, column=0, sticky=tk.W)
        self.description_entry = ttk.Entry(self.input_frame)
        self.description_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.input_frame, text="Kategori:").grid(row=2, column=0, sticky=tk.W)
        self.category_entry = ttk.Entry(self.input_frame)
        self.category_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.input_frame, text="Prioritas:").grid(row=3, column=0, sticky=tk.W)
        self.priority_combobox = ttk.Combobox(self.input_frame, values=["Rendah", "Sedang", "Tinggi"])
        self.priority_combobox.grid(row=3, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.input_frame, text="Deadline:").grid(row=4, column=0, sticky=tk.W)
        self.deadline_entry = DateEntry(self.input_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.deadline_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.input_frame, text="Jam:").grid(row=5, column=0, sticky=tk.W)
        self.hour_spinbox = tk.Spinbox(self.input_frame, from_=0, to=23, format="%02.0f")
        self.hour_spinbox.grid(row=5, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.input_frame, text="Menit:").grid(row=6, column=0, sticky=tk.W)
        self.minute_spinbox = tk.Spinbox(self.input_frame, from_=0, to=59, format="%02.0f")
        self.minute_spinbox.grid(row=6, column=1, sticky=(tk.W, tk.E))

        self.add_button = ttk.Button(self.input_frame, text="Tambah Tugas", command=self.add_task)
        self.add_button.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Frame for search and filter
        self.filter_frame = ttk.Frame(root, padding="10")
        self.filter_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(self.filter_frame, text="Cari:").grid(row=0, column=0, sticky=tk.W)
        self.search_entry = ttk.Entry(self.filter_frame)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        self.search_button = ttk.Button(self.filter_frame, text="Cari", command=self.search_tasks)
        self.search_button.grid(row=0, column=2, sticky=(tk.W, tk.E))
        
        ttk.Label(self.filter_frame, text="Kategori:").grid(row=1, column=0, sticky=tk.W)
        self.category_filter_entry = ttk.Entry(self.filter_frame)
        self.category_filter_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        self.filter_button = ttk.Button(self.filter_frame, text="Filter", command=self.filter_tasks)
        self.filter_button.grid(row=1, column=2, sticky=(tk.W, tk.E))
        
        ttk.Label(self.filter_frame, text="Status:").grid(row=2, column=0, sticky=tk.W)
        self.status_filter_combobox = ttk.Combobox(self.filter_frame, values=["semua", "belum selesai", "selesai"])
        self.status_filter_combobox.grid(row=2, column=1, sticky=(tk.W, tk.E))
        
        self.filter_status_button = ttk.Button(self.filter_frame, text="Filter", command=self.filter_by_status)
        self.filter_status_button.grid(row=2, column=2, sticky=(tk.W, tk.E))

        # Frame for task list
        self.tree_frame = ttk.Frame(root, padding="10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("Judul", "Deskripsi", "Kategori", "Prioritas", "Deadline", "Status"), show='headings')
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.heading("Prioritas", text="Prioritas")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        # Button frame
        self.button_frame = ttk.Frame(root, padding="10")
        self.button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        self.complete_button = ttk.Button(self.button_frame, text="Tandai Selesai", command=self.complete_task)
        self.complete_button.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        self.edit_button = ttk.Button(self.button_frame, text="Edit Tugas", command=self.edit_task)
        self.edit_button.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        self.delete_button = ttk.Button(self.button_frame, text="Hapus Tugas", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, sticky=(tk.W, tk.E))

        # Configure weights for resizing
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.refresh_tasks()
        self.task_notifications()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_combobox.get()
        deadline_date = self.deadline_entry.get_date().strftime("%d/%m/%Y")
        hour = self.hour_spinbox.get()
        minute = self.minute_spinbox.get()

        try:
            deadline = f"{deadline_date} {hour}:{minute}"
            deadline_datetime = datetime.strptime(deadline, "%d/%m/%Y %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal atau waktu tidak valid.")
            return

        new_task = Task(title, description, category, priority, deadline)
        self.tasks.add_task(new_task)
        self.refresh_tasks()

    def refresh_tasks(self):
        now = datetime.now()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks.get_tasks():
            deadline_datetime = datetime.strptime(task.deadline, "%d/%m/%Y %H:%M")
            if task.status == "selesai":
                color = "light green"
            elif (deadline_datetime - now).days <= 3:
                color = "red"
            elif (deadline_datetime - now).days <= 7:
                color = "yellow"
            else:
                color = ""
            
            self.tree.insert('', 'end', values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(task.status.replace(" ", "_"), color))

            # Configure tag colors
            if color:
                self.tree.tag_configure(color, background=color, foreground="black")

    def complete_task(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            task_values = self.tree.item(item, 'values')
            for task in self.tasks.get_tasks():
                if (task.title == task_values[0] and task.description == task_values[1] and
                    task.category == task_values[2] and task.priority == task_values[3] and
                    task.deadline == task_values[4]):
                    task.status = "selesai"
                    break
        self.refresh_tasks()

    def edit_task(self):
        selected_items = self.tree.selection()
        if len(selected_items) != 1:
            messagebox.showwarning("Peringatan", "Pilih satu tugas untuk diedit.")
            return

        selected_item = selected_items[0]
        task_values = self.tree.item(selected_item, 'values')
        for task in self.tasks.get_tasks():
            if (task.title == task_values[0] and task.description == task_values[1] and
                task.category == task_values[2] and task.priority == task_values[3] and
                task.deadline == task_values[4]):
                # Update the task with new values from input fields
                task.title = self.title_entry.get()
                task.description = self.description_entry.get()
                task.category = self.category_entry.get()
                task.priority = self.priority_combobox.get()
                deadline_date = self.deadline_entry.get_date().strftime("%d/%m/%Y")
                hour = self.hour_spinbox.get()
                minute = self.minute_spinbox.get()
                task.deadline = f"{deadline_date} {hour}:{minute}"
                
                # Refresh the tasks view
                self.refresh_tasks()
                break

    def delete_task(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            task_values = self.tree.item(item, 'values')
            for task in self.tasks.get_tasks():
                if (task.title == task_values[0] and task.description == task_values[1] and
                    task.category == task_values[2] and task.priority == task_values[3] and
                    task.deadline == task_values[4]):
                    self.tasks.remove_task(task)
                    break
        self.refresh_tasks()

    def search_tasks(self):
        search_term = self.search_entry.get().lower()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks.get_tasks():
            if search_term in task.title.lower() or search_term in task.description.lower():
                deadline_datetime = datetime.strptime(task.deadline, "%d/%m/%Y %H:%M")
                if task.status == "selesai":
                    color = "light green"
                elif (deadline_datetime - datetime.now()).days <= 3:
                    color = "red"
                elif (deadline_datetime - datetime.now()).days <= 7:
                    color = "yellow"
                else:
                    color = ""
                
                self.tree.insert('', 'end', values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(task.status.replace(" ", "_"), color))

                # Configure tag colors
                if color:
                    self.tree.tag_configure(color, background=color, foreground="black")

    def filter_tasks(self):
        filter_term = self.category_filter_entry.get().lower()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks.get_tasks():
            if filter_term in task.category.lower():
                deadline_datetime = datetime.strptime(task.deadline, "%d/%m/%Y %H:%M")
                if task.status == "selesai":
                    color = "light green"
                elif (deadline_datetime - datetime.now()).days <= 3:
                    color = "red"
                elif (deadline_datetime - datetime.now()).days <= 7:
                    color = "yellow"
                else:
                    color = ""
                
                self.tree.insert('', 'end', values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(task.status.replace(" ", "_"), color))

                # Configure tag colors
                if color:
                    self.tree.tag_configure(color, background=color, foreground="black")

    def filter_by_status(self):
        status_term = self.status_filter_combobox.get()
        if status_term == "semua":
            self.refresh_tasks()
            return
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks.get_tasks():
            if task.status == status_term:
                deadline_datetime = datetime.strptime(task.deadline, "%d/%m/%Y %H:%M")
                if task.status == "selesai":
                    color = "light green"
                elif (deadline_datetime - datetime.now()).days <= 3:
                    color = "red"
                elif (deadline_datetime - datetime.now()).days <= 7:
                    color = "yellow"
                else:
                    color = ""
                
                self.tree.insert('', 'end', values=(task.title, task.description, task.category, task.priority, task.deadline, task.status), tags=(task.status.replace(" ", "_"), color))

                # Configure tag colors
                if color:
                    self.tree.tag_configure(color, background=color, foreground="black")

    def task_notifications(self):
        now = datetime.now()
        upcoming_tasks = []
        for task in self.tasks.get_tasks():
            deadline_datetime = datetime.strptime(task.deadline, "%d/%m/%Y %H:%M")
            if now < deadline_datetime < now + timedelta(minutes=30):
                upcoming_tasks.append(task)
        if upcoming_tasks:
            notification_message = "Upcoming tasks:\n"
            for task in upcoming_tasks:
                notification_message += f"- {task.title} at {task.deadline}\n"
            messagebox.showinfo("Upcoming Tasks", notification_message)
        self.root.after(60000, self.task_notifications)


root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
