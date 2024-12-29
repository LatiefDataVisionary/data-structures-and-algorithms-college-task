import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import threading
import time

class Task:
    def __init__(self, title, description, category, priority, deadline):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.status = 'belum selesai'

    def mark_as_done(self):
        self.status = 'selesai'

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("800x600")
        self.root.configure(bg='#2E4053')
        
        self.tasks = LinkedList()

        # Frame untuk input
        input_frame = tk.Frame(root, bg='#2E4053')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Judul: ", bg='#2E4053', fg='#FDFEFE').grid(row=0, column=0)
        self.title_entry = tk.Entry(input_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.title_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Deskripsi: ", bg='#2E4053', fg='#FDFEFE').grid(row=1, column=0)
        self.description_entry = tk.Entry(input_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.description_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Kategori: ", bg='#2E4053', fg='#FDFEFE').grid(row=2, column=0)
        self.category_entry = tk.Entry(input_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.category_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Prioritas: ", bg='#2E4053', fg='#FDFEFE').grid(row=3, column=0)
        self.priority_entry = tk.Entry(input_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.priority_entry.grid(row=3, column=1)

        tk.Label(input_frame, text="Deadline (YYYY-MM-DD HH:MM): ", bg='#2E4053', fg='#FDFEFE').grid(row=4, column=0)
        self.deadline_entry = tk.Entry(input_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.deadline_entry.grid(row=4, column=1)

        tk.Button(input_frame, text="Tambah Tugas", command=self.add_task, bg='#5DADE2', fg='#2E4053').grid(row=5, columnspan=2, pady=10)

        # Frame untuk list tugas
        list_frame = tk.Frame(root, bg='#2E4053')
        list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(list_frame, width=100, height=10, bg='#34495E', fg='#FDFEFE', selectbackground='#5DADE2', selectforeground='#2E4053')
        self.task_listbox.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Frame untuk aksi
        action_frame = tk.Frame(root, bg='#2E4053')
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Lihat Tugas", command=self.view_tasks, bg='#58D68D', fg='#2E4053').grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Tandai Selesai", command=self.mark_task_done, bg='#58D68D', fg='#2E4053').grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Edit Tugas", command=self.edit_task, bg='#58D68D', fg='#2E4053').grid(row=0, column=2, padx=5)
        tk.Button(action_frame, text="Hapus Tugas", command=self.delete_task, bg='#58D68D', fg='#2E4053').grid(row=0, column=3, padx=5)

        # Frame untuk pencarian dan filter
        filter_frame = tk.Frame(root, bg='#2E4053')
        filter_frame.pack(pady=10)

        tk.Label(filter_frame, text="Cari: ", bg='#2E4053', fg='#FDFEFE').grid(row=0, column=0)
        self.search_entry = tk.Entry(filter_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.search_entry.grid(row=0, column=1)
        tk.Button(filter_frame, text="Cari", command=self.search_tasks, bg='#F4D03F', fg='#2E4053').grid(row=0, column=2, padx=5)

        tk.Label(filter_frame, text="Kategori: ", bg='#2E4053', fg='#FDFEFE').grid(row=1, column=0)
        self.category_filter_entry = tk.Entry(filter_frame, bg='#34495E', fg='#FDFEFE', insertbackground='#FDFEFE')
        self.category_filter_entry.grid(row=1, column=1)
        tk.Button(filter_frame, text="Filter", command=self.filter_tasks, bg='#F4D03F', fg='#2E4053').grid(row=1, column=2, padx=5)

        # Mulai thread notifikasi
        self.notification_thread = threading.Thread(target=self.task_notifications)
        self.notification_thread.daemon = True
        self.notification_thread.start()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_entry.get()
        deadline_str = self.deadline_entry.get()

        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            new_task = Task(title, description, category, priority, deadline)
            self.tasks.append(new_task)
            messagebox.showinfo("Success", "Tugas berhasil ditambahkan!")
            self.clear_entries()
            self.view_tasks()
        except ValueError:
            messagebox.showerror("Error", "Format tanggal tidak valid. Gunakan format YYYY-MM-DD HH:MM")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks.get_tasks():
            self.task_listbox.insert(tk.END, f"{task.title} - {task.category} - {task.priority} - {task.status} - {task.deadline}")

    def mark_task_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            tasks = self.tasks.get_tasks()
            tasks[index].mark_as_done()
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin ditandai selesai.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            tasks = self.tasks.get_tasks()
            task = tasks[index]

            new_title = simpledialog.askstring("Edit Judul", f"Judul ({task.title}):", initialvalue=task.title)
            new_description = simpledialog.askstring("Edit Deskripsi", f"Deskripsi ({task.description}):", initialvalue=task.description)
            new_category = simpledialog.askstring("Edit Kategori", f"Kategori ({task.category}):", initialvalue=task.category)
            new_priority = simpledialog.askstring("Edit Prioritas", f"Prioritas ({task.priority}):", initialvalue=task.priority)
            new_deadline_str = simpledialog.askstring("Edit Deadline", f"Deadline ({task.deadline.strftime('%Y-%m-%d %H:%M')}):", initialvalue=task.deadline.strftime('%Y-%m-%d %H:%M'))

            if new_deadline_str:
                try:
                    new_deadline = datetime.strptime(new_deadline_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    messagebox.showerror("Error", "Format tanggal tidak valid. Gunakan format YYYY-MM-DD HH:MM")
                    return
            else:
                new_deadline = task.deadline

            task.title = new_title if new_title else task.title
            task.description = new_description if new_description else task.description
            task.category = new_category if new_category else task.category
            task.priority = new_priority if new_priority else task.priority
            task.deadline = new_deadline

            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin diedit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            tasks = self.tasks.get_tasks()
            tasks.pop(index)
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Pilih tugas yang ingin dihapus.")

    def search_tasks(self):
        query = self.search_entry.get().lower()
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks.get_tasks():
            if query in task.title.lower() or query in task.description.lower():
                self.task_listbox.insert(tk.END, f"{task.title} - {task.category} - {task.priority} - {task.status} - {task.deadline}")

    def filter_tasks(self):
        category = self.category_filter_entry.get().lower()
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks.get_tasks():
            if category in task.category.lower():
                self.task_listbox.insert(tk.END, f"{task.title} - {task.category} - {task.priority} - {task.status} - {task.deadline}")

    def task_notifications(self):
        while True:
            now = datetime.now()
            for task in self.tasks.get_tasks():
                if task.status == 'belum selesai' and 0 < (task.deadline - now).total_seconds() <= 86400:
                    messagebox.showwarning("Peringatan Tugas", f"Tugas '{task.title}' mendekati batas waktu (kurang dari 24 jam).")
            time.sleep(3600)  # Periksa setiap jam

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
