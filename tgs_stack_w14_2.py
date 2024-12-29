class Stack:
    def __init__(self):
        self.items = []  # Inisialisasi stack sbg list kosong

    def is_empty(self):
        return self.items == []  # Mengecek apakah stack kosong

    def push(self, item):
        self.items.append(item)  # Menambahkan item ke stack

    def pop(self):
        return self.items.pop()  # Menghapus dan mengembalikan item teratas dari stack

    def peek(self):
        return self.items[-1]  # Mengembalikan item teratas dari stack tanpa menghapusnya

    def size(self):
        return len(self.items)  # Mengembalikan jumlah item dalam stack


class WebBrowser:
    def __init__(self):
        self.stack_belakang = Stack()  # Inisialisasi stack utk riwayat halaman sebelumnya
        self.stack_depan = Stack()  # Inisialisasi stack utk riwayat halaman berikutnya
        self.halaman_sekarang = None  # Halaman yang sdg dikunjungi saat ini

    def menu_utama(self):
        # Menampilkan menu utama
        print("\nMenu Utama:")
        print("1. Kunjungi Hal. Baru")
        print("2. Kembali ke Hal. Sebelumnya")
        print("3. Maju ke Hal.Berikutnya")
        print("4. Tampilkan Hal. Saat Ini")
        print("5. Tampilkan Jumlah Halaman dlm Riwayat")
        print("6. Untuk Keluar")

    def run(self):
        # Menjalankan program browser
        while True:
            self.menu_utama()
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                url = input("Masukkan URL halaman: ")
                self.kunjungi(url)
            elif pilihan == '2':
                self.kembali()
            elif pilihan == '3':
                self.maju()
            elif pilihan == '4':
                self.tampilkan_halaman()
            elif pilihan == '5':
                self.tampilkan_jumlah_halaman()
            elif pilihan == '6':
                print("Terima kasih telah menggunakan website kami.")
                break
            else:
                print("Pilihan tak valid, silakan pilih lagi.")

    def kunjungi(self, url):
        # Mengunjungi hal baru
        if self.halaman_sekarang:
            self.stack_belakang.push(self.halaman_sekarang)  # Menyimpan hal saat ini ke stack belakang
        self.halaman_sekarang = url  # Mengatur hal saat ini ke URL baru
        self.stack_depan = Stack()  # Menghapus riwayat hal berikutnya
        print("Halaman", url, "telah berhasil dikunjungi.")

    def kembali(self):
        # Kembali ke hal sebelumnya
        if not self.stack_belakang.is_empty():
            self.stack_depan.push(self.halaman_sekarang)  # Menyimpan halsaat ini ke stack depan
            self.halaman_sekarang = self.stack_belakang.pop()  # Mengambil hal terakhir dari stack belakang
            print("Kembali ke halaman:", self.halaman_sekarang)
        else:
            print("Tidak ada halaman di riwayat kembali.")

    def maju(self):
        # Maju ke hal berikutnya
        if not self.stack_depan.is_empty():
            self.stack_belakang.push(self.halaman_sekarang)  # Menyimpan halaman saat ini ke stack belakang
            self.halaman_sekarang = self.stack_depan.pop()  # Mengambil halaman terakhir dari stack depan
            print("Maju ke halaman:", self.halaman_sekarang)
        else:
            print("Tidak ada halaman di riwayat maju.")

    def tampilkan_halaman(self):
        # Utk menampilkan halaman saat ini
        print("Halaman saat ini:", self.halaman_sekarang)

    def tampilkan_jumlah_halaman(self):
        # Utk menampilkan jumlah halaman dlm riwayat (stack belakang dan stack depan)
        total_halaman = self.stack_belakang.size() + self.stack_depan.size()
        print("Jumlah halaman dalam riwayat:", total_halaman)


# Main Program
if __name__ == "__main__":
    browser = WebBrowser()  # Utk membuat objek WebBrowser
    browser.run()  # Utk menjalankan program browser


'''Kode di atas adalah implementasi sederhana dari 
sebuah web browser yang menggunakan struktur data 
Stack/tumpukan untuk mengelola riwayat penelusuran'''

# Contoh Penggunaan: 
'''Mengunjungi website e learning uty (menggunakan 
menu no. 1 untuk memasukkan url dibawh ini)
1. elearning-uty (stack terbawah)
2. struktur-data-algortima
3. topic-14
4. tgs-p14
5. soal-tgs-p14 (stack teratas)
'''

# Contoh dlm menu
'''Menu Utama:
1. Kunjungi Halaman Baru
2. Kembali ke Halaman Sebelumnya
3. Maju ke Halaman Berikutnya
4. Tampilkan Halaman Saat Ini
5. Tampilkan Jumlah Halaman dalam Riwayat
6. Keluar
Pilih menu: 1
Masukkan URL halaman: elearning-uty
Halaman elearning-uty telah berhasil dikunjungi.'''
