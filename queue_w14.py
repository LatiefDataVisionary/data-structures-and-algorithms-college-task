class BankQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"{customer} telah masuk antrian.")
            
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        customer = self.queue.pop(0)
        print(f"{customer} telah dilayani.")
        return customer
    
    def peek(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        return self.queue[0]
    
    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
            return
        print("antrian saat ini:")
        for customer in self.queue:
            print(customer)
            
            
# Buat objek antrian bank
bank_queue = BankQueue()

# Tambahkan pelanggan ke antrian
bank_queue.enqueue("Rama")
bank_queue.enqueue("John")
bank_queue.enqueue("Jane")
bank_queue.enqueue("Doe")

# Tampilkan pelanggan yg berada didepan antrian
print("Pelanggan yang berada di depan antrian:", bank_queue.peek())
    
# Layani pelanggan 
served_customer = bank_queue.dequeue()
print("Pelanggan yg dilayani: ", served_customer)
    
# Tampilkan antrian saat ini
bank_queue.display()
    
    


























