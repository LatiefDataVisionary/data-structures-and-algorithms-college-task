import struct

# Format untuk data alamat
alamat_format = '50s10s30s20s20s50s'  # Nama Dusun, RT/RW, Kel/Desa, Kecamatan, Kabupaten, Provinsi
# alamat_format = '500s100s300s200s200s500s'

# Format untuk data KTP, dengan alamat sebagai bagian dari KTP
ktp_format = '50s50s20s10s30s20s20s50s10s30s20s20s50s'  # NIK, Nama, Tempat Lahir, Tanggal Lahir, Jenis Kelamin, Agama, Status Perkawinan, Pekerjaan, Kewarganegaraan, Alamat
# ktp_format = '500s500s200s100s300s200s200s500s100s300s200s200s500s'

def input_alamat_data():
    # Input data alamat dari pengguna
    print("\n\t\t" + "=" * 3 + "Silahkan Masukkan Data Alamat" + "=" * 3)
    dusun = input("\t\tMasukkan nama Dusun: ").title()
    rt_rw = input("\t\tMasukkan RT/RW: ").title()
    kel_desa = input("\t\tMasukkan Kelurahan/Desa: ").title()
    kecamatan = input("\t\tMasukkan Kecamatan: ").title()
    kabupaten = input("\t\tMasukkan Kabupaten: ").title()
    provinsi = input("\t\tMasukkan Provinsi: ").title()

    # Kemas data alamat menggunakan struct.pack
    alamat_data = struct.pack(alamat_format, dusun.encode(), rt_rw.encode(), kel_desa.encode(), kecamatan.encode(), kabupaten.encode(), provinsi.encode())
    return alamat_data

def input_ktp_data():
    # Input data KTP dari pengguna
    print("=" * 5 + "Silahkan Masukkan Data KTP" + "=" * 5)
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ").title()
    tempat_lahir = input("Masukkan Tempat Lahir: ").title()
    tgl_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")  # Pastikan format tanggal lahir sesuai
    jenis_kelamin = input("Masukkan Jenis Kelamin: ").title()
    agama = input("Masukkan Agama: ").title()
    status_perkawinan = input("Masukkan Status Perkawinan: ").title()
    pekerjaan = input("Masukkan Pekerjaan: ").title()
    kewarganegaraan = input("Masukkan Kewarganegaraan: ").title()

    # Input data alamat
    alamat_data = input_alamat_data()

    # Kemas data KTP menggunakan struct.pack, dengan alamat sebagai bagian dari KTP
    ktp_data = struct.pack(ktp_format, nik.encode(), nama.encode(), tempat_lahir.encode(), tgl_lahir.encode(), jenis_kelamin.encode(), agama.encode(), status_perkawinan.encode(), pekerjaan.encode(), kewarganegaraan.encode(), alamat_data)
    return ktp_data

def unpack_alamat_data(alamat_data):
    # Unpack data alamat menggunakan struct.unpack
    dusun, rt_rw, kel_desa, kecamatan, kabupaten, provinsi = struct.unpack(alamat_format, alamat_data)
    return {
        'dusun': dusun.decode().strip(),
        'rt_rw': rt_rw.decode().strip(),
        'kel_desa': kel_desa.decode().strip(),
        'kecamatan': kecamatan.decode().strip(),
        'kabupaten': kabupaten.decode().strip(),
        'provinsi': provinsi.decode().strip()
    }

def unpack_ktp_data(ktp_data):
    # Unpack data KTP menggunakan struct.unpack
    nik, nama, tempat_lahir, tgl_lahir, jenis_kelamin, agama, status_perkawinan, pekerjaan, kewarganegaraan, alamat_data = struct.unpack(ktp_format, ktp_data)
    # Unpack data alamat dari bagian KTP
    alamat_info = unpack_alamat_data(alamat_data)
    return {
        'nik': nik.decode().strip(),
        'nama': nama.decode().strip(),
        'tempat_lahir': tempat_lahir.decode().strip(),
        'tgl_lahir': tgl_lahir.decode().strip(),
        'jenis_kelamin': jenis_kelamin.decode().strip(),
        'agama': agama.decode().strip(),
        'status_perkawinan': status_perkawinan.decode().strip(),
        'pekerjaan': pekerjaan.decode().strip(),
        'kewarganegaraan': kewarganegaraan.decode().strip(),
        'alamat': alamat_info
    }

def main():
    # Input data KTP
    ktp_data = input_ktp_data()

    # Tampilkan data yang telah di-unpack
    ktp_info = unpack_ktp_data(ktp_data)
    print("\nData KTP:")
    print(f"NIK                 : {ktp_info['nik']}")
    print(f"Nama                : {ktp_info['nama']}")
    print(f"Tempat Lahir        : {ktp_info['tempat_lahir']}")
    print(f"Tanggal Lahir       : {ktp_info['tgl_lahir']}")
    print(f"Jenis Kelamin       : {ktp_info['jenis_kelamin']}")
    print(f"Agama               : {ktp_info['agama']}")
    print(f"Status Perkawinan   : {ktp_info['status_perkawinan']}")
    print(f"Pekerjaan           : {ktp_info['pekerjaan']}")
    print(f"Kewarganegaraan     : {ktp_info['kewarganegaraan']}")
    print("Alamat               :")
    print(f"                      -Dusun              : {ktp_info['alamat']['dusun']}")
    print(f"                      -RT/RW              : {ktp_info['alamat']['rt_rw']}")
    print(f"                      -Kelurahan/Desa     : {ktp_info['alamat']['kel_desa']}")
    print(f"                      -Kecamatan          : {ktp_info['alamat']['kecamatan']}")
    print(f"                      -Kabupaten          : {ktp_info['alamat']['kabupaten']}")
    print(f"                      -Provinsi           : {ktp_info['alamat']['provinsi']}")

if __name__ == "__main__":
    main()
