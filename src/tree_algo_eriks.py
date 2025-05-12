import tkinter as tk

class TreeNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeVisualizer:
    def _init_(self, root):
        self.root = root
        self.node_radius = 20
        self.node_distance_x = 50
        self.node_distance_y = 50
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.grid(row=1, column=0, columnspan=5)
        self.tree_root = None  # Initially, no root node
        self.create_widgets()

    def set_root_node(self):
        data = self.root_input_box.get()
        if not data:
            self.output_label.config(text="Data root tidak boleh kosong!")
            return
        self.tree_root = TreeNode(data)
        self.canvas.delete("all")
        self.draw_tree(self.tree_root, 400, 30, 200)
        self.output_label.config(text=f"Root node {data} telah ditambahkan.")

    def insert_node(self, current_node, target, data, direction):
        if current_node is None:
            return False
        
        if current_node.data == target:
            new_node = TreeNode(data)
            if direction == "kiri":
                if current_node.left is None:
                    current_node.left = new_node
                else:
                    self.output_label.config(text=f"Node {target} sudah memiliki anak kiri.")
            elif direction == "kanan":
                if current_node.right is None:
                    current_node.right = new_node
                else:
                    self.output_label.config(text=f"Node {target} sudah memiliki anak kanan.")
            return True
        else:
            return self.insert_node(current_node.left, target, data, direction) or self.insert_node(current_node.right, target, data, direction)

    def add_child_node(self):
        if self.tree_root is None:
            self.output_label.config(text="Root node belum diatur!")
            return
        
        target = self.target_box.get()
        data = self.child_input_box.get()
        direction = self.direction_box.get().lower()
        if self.insert_node(self.tree_root, target, data, direction):
            self.canvas.delete("all")
            self.draw_tree(self.tree_root, 400, 30, 200)
            self.output_label.config(text=f"Node {data} telah ditambahkan ke {direction} dari {target}.")
        else:
            self.output_label.config(text=f"Node target {target} tidak ditemukan.")

    def edit_node(self, current_node, target, new_data):
        if current_node is None:
            return False
        
        if current_node.data == target:
            current_node.data = new_data
            return True
        else:
            return self.edit_node(current_node.left, target, new_data) or self.edit_node(current_node.right, target, new_data)

    def edit_node_action(self):
        target = self.edit_target_box.get()
        new_data = self.edit_data_box.get()
        if self.edit_node(self.tree_root, target, new_data):
            self.canvas.delete("all")
            self.draw_tree(self.tree_root, 400, 30, 200)
            self.output_label.config(text=f"Node {target} telah diubah menjadi {new_data}.")
        else:
            self.output_label.config(text=f"Node target {target} tidak ditemukan.")

    def delete_node(self, current_node, parent, target):
        if current_node is None:
            return False
        
        if current_node.data == target:
            if current_node.left is None and current_node.right is None:
                if parent.left == current_node:
                    parent.left = None
                elif parent.right == current_node:
                    parent.right = None
            else:
                self.output_label.config(text="Node tidak dapat dihapus karena memiliki anak.")
            return True
        else:
            return self.delete_node(current_node.left, current_node, target) or self.delete_node(current_node.right, current_node, target)

    def delete_node_action(self):
        target = self.delete_target_box.get()
        if self.tree_root and self.tree_root.data == target:
            self.output_label.config(text="Root node tidak dapat dihapus!")
            return
        
        if self.delete_node(self.tree_root, None, target):
            self.canvas.delete("all")
            self.draw_tree(self.tree_root, 400, 30, 200)
            self.output_label.config(text=f"Node {target} telah dihapus.")
        else:
            self.output_label.config(text=f"Node target {target} tidak ditemukan atau memiliki anak.")

    def search_node(self, current_node, target):
        if current_node is None:
            return None
        if current_node.data == target:
            return current_node
        left_search = self.search_node(current_node.left, target)
        if left_search:
            return left_search
        return self.search_node(current_node.right, target)

    def search_node_action(self):
        target = self.search_target_box.get()
        node = self.search_node(self.tree_root, target)
        if node:
            self.output_label.config(text=f"Node dengan data '{target}' ditemukan.")
        else:
            self.output_label.config(text=f"Node dengan data '{target}' tidak ditemukan.")

    def draw_tree(self, node, x, y, x_offset):
        if node is None:
            return
        self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill="white")
        self.canvas.create_text(x, y, text=node.data)
        if node.left:
            self.canvas.create_line(x, y, x - x_offset, y + self.node_distance_y)
            self.draw_tree(node.left, x - x_offset, y + self.node_distance_y, x_offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + x_offset, y + self.node_distance_y)
            self.draw_tree(node.right, x + x_offset, y + self.node_distance_y, x_offset // 2)

    def create_widgets(self):
        # Main Frame for Input, Edit, Delete sections
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, columnspan=5, sticky="n")

        # Root Node Input Section
        self.root_frame = tk.LabelFrame(self.main_frame, text="Root Node")
        self.root_frame.grid(row=0, column=0, padx=10, pady=10)

        self.root_input_label = tk.Label(self.root_frame, text="Masukkan data root:")
        self.root_input_label.pack()
        self.root_input_box = tk.Entry(self.root_frame)
        self.root_input_box.pack()
        self.set_root_button = tk.Button(self.root_frame, text="Set Root Node", command=self.set_root_node)
        self.set_root_button.pack()

        # Child Node Input Section
        self.child_frame = tk.LabelFrame(self.main_frame, text="Child Node")
        self.child_frame.grid(row=0, column=1, padx=10, pady=10)

        self.child_input_label = tk.Label(self.child_frame, text="Masukkan data child node:")
        self.child_input_label.pack()
        self.child_input_box = tk.Entry(self.child_frame)
        self.child_input_box.pack()
        self.target_label = tk.Label(self.child_frame, text="Masukkan data node target:")
        self.target_label.pack()
        self.target_box = tk.Entry(self.child_frame)
        self.target_box.pack()
        self.direction_label = tk.Label(self.child_frame, text="Ingin menambahkan ke kiri atau kanan? (kiri/kanan):")
        self.direction_label.pack()
        self.direction_box = tk.Entry(self.child_frame)
        self.direction_box.pack()
        self.add_child_button = tk.Button(self.child_frame, text="Tambah Child Node", command=self.add_child_node)
        self.add_child_button.pack()

        # Edit Node Section
        self.edit_frame = tk.LabelFrame(self.main_frame, text="Edit Node")
        self.edit_frame.grid(row=0, column=2, padx=10, pady=10)

        self.edit_target_label = tk.Label(self.edit_frame, text="Masukkan data node target:")
        self.edit_target_label.pack()
        self.edit_target_box = tk.Entry(self.edit_frame)
        self.edit_target_box.pack()
        self.edit_data_label = tk.Label(self.edit_frame, text="Masukkan data baru:")
        self.edit_data_label.pack()
        self.edit_data_box = tk.Entry(self.edit_frame)
        self.edit_data_box.pack()
        self.edit_button = tk.Button(self.edit_frame, text="Edit Node", command=self.edit_node_action)
        self.edit_button.pack()

        # Delete Node Section
        self.delete_frame = tk.LabelFrame(self.main_frame, text="Hapus Node")
        self.delete_frame.grid(row=0, column=3, padx=10, pady=10)

        self.delete_target_label = tk.Label(self.delete_frame, text="Masukkan data node target:")
        self.delete_target_label.pack()
        self.delete_target_box = tk.Entry(self.delete_frame)
        self.delete_target_box.pack()
        self.delete_button = tk.Button(self.delete_frame, text="Hapus Node", command=self.delete_node_action)
        self.delete_button.pack()

        # Search Node Section
        self.search_frame = tk.LabelFrame(self.main_frame, text="Cari Node")
        self.search_frame.grid(row=0, column=4, padx=10, pady=10)

        self.search_target_label = tk.Label(self.search_frame, text="Masukkan data node yang dicari:")
        self.search_target_label.pack()
        self.search_target_box = tk.Entry(self.search_frame)
        self.search_target_box.pack()
        self.search_button = tk.Button(self.search_frame, text="Cari Node", command=self.search_node_action)
        self.search_button.pack()

        # Output Label
        self.output_label = tk.Label(self.root, text="")
        self.output_label.grid(row=2, column=0, columnspan=5)

root = tk.Tk()
root.title("Visualisasi Pohon")

visualizer = BinaryTreeVisualizer(root)

root.mainloop()
