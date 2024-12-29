import struct

# Definisikan format data Alamat
alamat_format = '30s10s20s20s20s30s'  # 30 karakter untuk nama dusun, 10 karakter untuk RT/RW, 20 karakter untuk kel/desa, kecamatan, kabupaten, dan provinsi

# Definisikan format data KTP dengan turunan dari Alamat
ktp_format = '20s30s20s30s20s10s20s20s20s30s30s' + alamat_format  # NIK, nama, tempat_lahir, tgl_lahir, jenis_kelamin, agama, status_perkawinan, pekerjaan, kewarganegaraan, diikuti oleh data alamat

def input_alamat_data():
    # Input data alamat dari pengguna
    dusun = input("Masukkan Dusun: ")
    rt_rw = input("Masukkan RT/RW: ")
    kel_desa = input("Masukkan Kelurahan/Desa: ")
    kecamatan = input("Masukkan Kecamatan: ")
    kabupaten = input("Masukkan Kabupaten: ")
    provinsi = input("Masukkan Provinsi: ")

    # Kemas data alamat menggunakan struct.pack
    alamat_data = struct.pack(alamat_format, dusun.encode(), rt_rw.encode(), kel_desa.encode(), kecamatan.encode(), kabupaten.encode(), provinsi.encode())
    return alamat_data

def input_ktp_data():
    # Input data KTP dari pengguna
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan nama: ")
    tempat_lahir = input("Masukkan tempat lahir: ")
    tgl_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
    jenis_kelamin = input("Masukkan jenis kelamin: ")
    agama = input("Masukkan agama: ")
    status_perkawinan = input("Masukkan status perkawinan: ")
    pekerjaan = input("Masukkan pekerjaan: ")
    kewarganegaraan = input("Masukkan kewarganegaraan: ")

    # Input data alamat
    alamat_data = input_alamat_data()

    # Kemas data KTP menggunakan struct.pack
    ktp_data = struct.pack(ktp_format, nik.encode(), nama.encode(), tempat_lahir.encode(), tgl_lahir.encode(), jenis_kelamin.encode(), agama.encode(), status_perkawinan.encode(), pekerjaan.encode(), kewarganegaraan.encode(), alamat_data)
    return ktp_data

def unpack_ktp_data(ktp_data):
    # Unpack data KTP menggunakan struct.unpack
    ktp_info = struct.unpack(ktp_format, ktp_data)

    # Unpack data alamat dari turunan KTP
    alamat_info = struct.unpack(alamat_format, ktp_info[-len(alamat_format):])

    return {
        'NIK': ktp_info[0].decode().strip(),
        'nama': ktp_info[1].decode().strip(),
        'tempat_lahir': ktp_info[2].decode().strip(),
        'tgl_lahir': ktp_info[3].decode().strip(),
        'jenis_kelamin': ktp_info[4].decode().strip(),
        'agama': ktp_info[5].decode().strip(),
        'status_perkawinan': ktp_info[6].decode().strip(),
        'pekerjaan': ktp_info[7].decode().strip(),
        'kewarganegaraan': ktp_info[8].decode().strip(),
        'alamat': {
            'dusun': alamat_info[0].decode().strip(),
            'rt_rw': alamat_info[1].decode().strip(),
            'kel_desa': alamat_info[2].decode().strip(),
            'kecamatan': alamat_info[3].decode().strip(),
            'kabupaten': alamat_info[4].decode().strip(),
            'provinsi': alamat_info[5].decode().strip()
        }
    }

def main():
    # Input data KTP
    ktp_data = input_ktp_data()

    # Tampilkan data yang telah di-unpack
    ktp_info = unpack_ktp_data(ktp_data)
    print("\nData KTP:")
    print(f"NIK: {ktp_info['NIK']}")
    print(f"Nama: {ktp_info['nama']}")
    print(f"Tempat/Tanggal Lahir: {ktp_info['tempat_lahir']}, {ktp_info['tgl_lahir']}")
    print(f"Jenis Kelamin: {ktp_info['jenis_kelamin']}")
    print(f"Agama: {ktp_info['agama']}")
    print(f"Status Perkawinan: {ktp_info['status_perkawinan']}")
    print(f"Pekerjaan: {ktp_info['pekerjaan']}")
    print(f"Kewarganegaraan: {ktp_info['kewarganegaraan']}")
    print("Alamat:")
    print(f"  Dusun: {ktp_info['alamat']['dusun']}")
    print(f"  RT/RW: {ktp_info['alamat']['rt_rw']}")
    print(f"  Kel/Desa: {ktp_info['alamat']['kel_desa']}")
    print(f"  Kecamatan: {ktp_info['alamat']['kecamatan']}")
    print(f"  Kabupaten: {ktp_info['alamat']['kabupaten']}")
    print(f"  Provinsi: {ktp_info['alamat']['provinsi']}")

if __name__ == "__main__":
    main()
