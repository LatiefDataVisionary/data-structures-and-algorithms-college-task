class RumahMakanMiAyam:
    def __init__(self):
        self.antrian_makanan = []  
        self.antrian_minuman = []  
        self.menu_makanan = {}  
        self.menu_minuman = {}  

    def is_empty(self, tipe):
        # Cek apakah antrian kosong berdasarkan tipe (makanan atau minuman)
        if tipe == "makanan":
            return len(self.antrian_makanan) == 0
        elif tipe == "minuman":
            return len(self.antrian_minuman) == 0

    def tambah_pesanan(self, tipe, nomor_pesanan):
        # menambahkan pesanan ke antrian berdasarkan tipe dan nomor pesanan
        if tipe == "makanan" and nomor_pesanan in self.menu_makanan:
            pesanan = self.menu_makanan[nomor_pesanan]
            self.antrian_makanan.append(pesanan)
            print(f"{pesanan} telah masuk antrian makanan.")
        elif tipe == "minuman" and nomor_pesanan in self.menu_minuman:
            pesanan = self.menu_minuman[nomor_pesanan]
            self.antrian_minuman.append(pesanan)
            print(f"{pesanan} telah masuk antrian minuman.")
        else:
            print("Nomor pesanan tidak valid.")

    def proses_pesanan(self, tipe):
        # utk memproses pesanan dari antrian berdasarkan tipe
        if self.is_empty(tipe):
            print(f"Antrian {tipe} kosong.")
            return None
        if tipe == "makanan":
            pesanan_selesai = self.antrian_makanan.pop(0)
            print(f"{pesanan_selesai} telah selesai diproses.")
            return pesanan_selesai
        elif tipe == "minuman":
            pesanan_selesai = self.antrian_minuman.pop(0)
            print(f"{pesanan_selesai} telah selesai diproses.")
            return pesanan_selesai

    def lihat_antrian(self, tipe):
        # utk melihat antrian saat ini berdasarkan tipe
        if self.is_empty(tipe):
            print(f"Antrian {tipe} kosong.")
            return
        if tipe == "makanan":
            print("Antrian makanan saat ini:")
            for idx, pesanan in enumerate(self.antrian_makanan, start=1):
                print(f"{idx}. {pesanan}")
        elif tipe == "minuman":
            print("Antrian minuman saat ini:")
            for idx, pesanan in enumerate(self.antrian_minuman, start=1):
                print(f"{idx}. {pesanan}")

    def tampilkan_menu(self, tipe):
        # menampilkan menu berdasarkan tipe (makanan atau minuman)
        if tipe == "makanan":
            print("Menu Mie Ayam:")
            for nomor, (makanan, harga) in self.menu_makanan.items():
                print(f"{nomor}. {makanan}: Rp {harga}")
        elif tipe == "minuman":
            print("Menu Minuman:")
            for nomor, (minuman, harga) in self.menu_minuman.items():
                print(f"{nomor}. {minuman}: Rp {harga}")

    def sub_menu_makanan(self):
        # sub menu untuk pesanan makanan
        while True:
            print("\nMenu Makanan:")
            print("1. Tambah Pesanan Makanan")
            print("2. Proses Pesanan Makanan")
            print("3. Lihat Antrian Makanan")
            print("4. Kembali ke Menu Utama")

            pilihan = input("Masukkan pilihan menu: ")

            if pilihan == '1':
                self.tampilkan_menu("makanan")
                try:
                    nomor_pesanan = int(input("Masukkan nomor menu Mie Ayam: "))
                    self.tambah_pesanan("makanan", nomor_pesanan)
                except ValueError:
                    print("Input tidak valid. Silakan masukkan nomor pesanan yang benar.")
            elif pilihan == '2':
                self.proses_pesanan("makanan")
            elif pilihan == '3':
                self.lihat_antrian("makanan")
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

    def sub_menu_minuman(self):
        # sub menu untuk pesanan minuman
        while True:
            print("\nMenu Minuman:")
            print("1. Tambah Pesanan Minuman")
            print("2. Proses Pesanan Minuman")
            print("3. Lihat Antrian Minuman")
            print("4. Kembali ke Menu Utama")

            pilihan = input("Masukkan pilihan menu: ")

            if pilihan == '1':
                self.tampilkan_menu("minuman")
                try:
                    nomor_pesanan = int(input("Masukkan nomor menu Minuman: "))
                    self.tambah_pesanan("minuman", nomor_pesanan)
                except ValueError:
                    print("Input tidak valid. Silakan masukkan nomor pesanan yang benar.")
            elif pilihan == '2':
                self.proses_pesanan("minuman")
            elif pilihan == '3':
                self.lihat_antrian("minuman")
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

    def menu_utama(self):
        # Menu utamanya
        while True:
            print("\nMenu Utama Rumah Makan Mi Ayam Pak Rafi:")
            print("1. Menu Makanan")
            print("2. Menu Minuman")
            print("3. Keluar")

            pilihan = input("Masukkan pilihan menu: ")

            if pilihan == '1':
                self.sub_menu_makanan()
            elif pilihan == '2':
                self.sub_menu_minuman()
            elif pilihan == '3':
                print("Terima kasih telah mengunjungi Rumah Makan Mi Ayam Pak Rafi!!.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
            input("Tekan Enter untuk melanjutkan...")

# Inisialisasi Rumah Makan Mi Ayam
rumah_makan = RumahMakanMiAyam()

# Menu Makanan dan Minuman
rumah_makan.menu_makanan = {
    1: ('Miayam Original', 15000),
    2: ('Miayam Pedas', 17000),
    3: ('Miayam Bakso', 21000),
    4: ('Miayam Pangsit', 17000),
    5: ('Miayam Ceker', 16000),
    6: ('Miayam Goreng', 15000),
    7: ('Miayam Tetelan', 23000),
    8: ('Miayam Komplit', 25000),
    9: ('Miayam Jumbo', 25000)
}

rumah_makan.menu_minuman = {
    1: ('Es Teh Manis', 5000),
    2: ('Es Jeruk', 6000),
    3: ('Es Campur', 8000),
    4: ('Es Cincau', 7000),
    5: ('Air Mineral', 3000)
}

# utk menjalankan kode
rumah_makan.menu_utama()
