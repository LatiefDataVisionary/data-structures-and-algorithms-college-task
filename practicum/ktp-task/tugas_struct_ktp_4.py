import struct
from tabulate import tabulate

# Format untuk data alamat
alamat_format = '50s10s30s20s20s50s'  # Nama Dusun, RT/RW, Kel/Desa, Kecamatan, Kabupaten, Provinsi

# Format untuk data KTP, dengan alamat sebagai bagian dari KTP
ktp_format = '50s50s20s10s30s20s20s50s10s30s20s20s50s'  # NIK, Nama, Tempat Lahir, Tanggal Lahir, Jenis Kelamin, Agama, Status Perkawinan, Pekerjaan, Kewarganegaraan, Alamat

def input_alamat_data():
    # Input data alamat dari pengguna
    print("\n\t\t" + "=" * 3 + "Silahkan Masukkan Data Alamat" + "=" * 3)
    dusun = input("\t\tMasukkan nama Dusun: ").capitalize()
    rt_rw = input("\t\tMasukkan RT/RW: ").capitalize()
    kel_desa = input("\t\tMasukkan Kelurahan/Desa: ").capitalize()
    kecamatan = input("\t\tMasukkan Kecamatan: ").capitalize()
    kabupaten = input("\t\tMasukkan Kabupaten: ").capitalize()
    provinsi = input("\t\tMasukkan Provinsi: ").capitalize()

    # Kemas data alamat menggunakan struct.pack
    alamat_data = struct.pack(alamat_format, dusun.encode(), rt_rw.encode(), kel_desa.encode(), kecamatan.encode(), kabupaten.encode(), provinsi.encode())
    return alamat_data

def input_ktp_data():
    # Input data KTP dari pengguna
    print("=" * 5 + "Silahkan Masukkan Data KTP" + "=" * 5)
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")
    tempat_lahir = input("Masukkan Tempat Lahir: ")
    tgl_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
    jenis_kelamin = input("Masukkan Jenis Kelamin: ")
    agama = input("Masukkan Agama: ")
    status_perkawinan = input("Masukkan Status Perkawinan: ")
    pekerjaan = input("Masukkan Pekerjaan: ")
    kewarganegaraan = input("Masukkan Kewarganegaraan: ")

    # Input data alamat
    alamat_data = input_alamat_data()

    # Kemas data KTP menggunakan struct.pack, dengan alamat sebagai bagian dari KTP
    ktp_data = struct.pack(ktp_format, nik.encode(), nama.encode(), tempat_lahir.encode(), tgl_lahir.encode(), jenis_kelamin.encode(), agama.encode(), status_perkawinan.encode(), pekerjaan.encode(), kewarganegaraan.encode(), alamat_data)
    return ktp_data

def unpack_alamat_data(alamat_data):
    # Unpack data alamat menggunakan struct.unpack
    dusun, rt_rw, kel_desa, kecamatan, kabupaten, provinsi = struct.unpack(alamat_format, alamat_data)
    return {
        'Dusun': dusun.decode().strip(),
        'RT/RW': rt_rw.decode().strip(),
        'Kelurahan/Desa': kel_desa.decode().strip(),
        'Kecamatan': kecamatan.decode().strip(),
        'Kabupaten': kabupaten.decode().strip(),
        'Provinsi': provinsi.decode().strip()
    }

def unpack_ktp_data(ktp_data):
    # Unpack data KTP menggunakan struct.unpack
    nik, nama, tempat_lahir, tgl_lahir, jenis_kelamin, agama, status_perkawinan, pekerjaan, kewarganegaraan, alamat_data = struct.unpack(ktp_format, ktp_data)
    # Unpack data alamat dari bagian KTP
    alamat_info = unpack_alamat_data(alamat_data)
    return {
        'NIK': nik.decode().strip(),
        'Nama': nama.decode().strip(),
        'Tempat Lahir': tempat_lahir.decode().strip(),
        'Tanggal Lahir': tgl_lahir.decode().strip(),
        'Jenis Kelamin': jenis_kelamin.decode().strip(),
        'Agama': agama.decode().strip(),
        'Status Perkawinan': status_perkawinan.decode().strip(),
        'Pekerjaan': pekerjaan.decode().strip(),
        'Kewarganegaraan': kewarganegaraan.decode().strip(),
        'Alamat': alamat_info
    }

def main():
    # Input data KTP
    ktp_data = input_ktp_data()

    # Tampilkan data yang telah di-unpack
    ktp_info = unpack_ktp_data(ktp_data)
    print("\nData KTP:")
    table_data = []
    for key, value in ktp_info.items():
        if key == 'Alamat':
            for alamat_key, alamat_value in value.items():
                table_data.append([alamat_key, alamat_value])
        else:
            table_data.append([key, value])

    print(tabulate(table_data, headers=["Field", "Value"]))

if __name__ == "__main__":
    main()
