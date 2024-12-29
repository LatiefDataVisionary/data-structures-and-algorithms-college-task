import struct

# Definisikan format data KTP
# Misalnya, kita anggap KTP memiliki nama (string), alamat (string), dan nomor KTP (integer)
ktp_format = '50s50si'  # 50 karakter untuk nama dan alamat, diikuti oleh 1 integer

def input_ktp_data():
    # Input data dari pengguna
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    nomor_ktp = int(input("Masukkan nomor KTP: "))

    # Kemas data menggunakan struct.pack
    ktp_data = struct.pack(ktp_format, nama.encode(), alamat.encode(), nomor_ktp)
    return ktp_data

def unpack_ktp_data(ktp_data):
    # Unpack data menggunakan struct.unpack
    nama, alamat, nomor_ktp = struct.unpack(ktp_format, ktp_data)
    return {
        'nama': nama.decode().strip(),
        'alamat': alamat.decode().strip(),
        'nomor_ktp': nomor_ktp
    }

def main():
    # Input data KTP
    ktp_data = input_ktp_data()

    # Tampilkan data yang telah di-unpack
    ktp_info = unpack_ktp_data(ktp_data)
    print("\nData KTP:")
    print(f"Nama: {ktp_info['nama']}")
    print(f"Alamat: {ktp_info['alamat']}")
    print(f"Nomor KTP: {ktp_info['nomor_ktp']}")

if __name__ == "__main__":
    main()
