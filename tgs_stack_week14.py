class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    
class WebBrowser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.hal_saat_ini = None
        
    def kunjungi(self, url):
        if self.hal_saat_ini:
            self.back_stack.push(self.hal_saat_ini)
        self.hal_saat_ini = url
        self.forward_stack = Stack()
        self.tampilkan_halaman()
        
    def kembali(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.hal_saat_ini)
            self.hal_data_ini = self.back_stack.pop()
            self.tampilkan_halaman()
        else:
            print("Tidak ada halaman di riwayat kembali.")
            
    def maju(self):
        if not self.forward_stack.isempty():
            self.back_stack.push(self.hal_saat_ini)
            self.hal_saat_ini = self.forward_stack.pop()
            self.tampilkan_halaman()
        else:
            print("Tidak ada halaman di riwayat maju.")
            
    def tampilkan_halaman(self):
        print("Halaman saat ini:", self.hal_saat_ini)
        
        
# Contoh penggunaan 
browser = WebBrowser()
print()

# Mulai menumpuk stack  
browser.kunjungi("elearning-uty. com")
browser.kunjungi("struktur-data .com")
browser.kunjungi("tgs-p14 .com")
browser.kunjungi("tugas_stack .com")
print()

# Mengeluarkan Stack
browser.kembali()
browser.kembali()
# browser.maju()
# browser.kunjungi("halaman4.com")
# brwoser.kunjungi("h")
browser.kembali()
browser.kembali()
    
    
    
    
    
    
    
    
    