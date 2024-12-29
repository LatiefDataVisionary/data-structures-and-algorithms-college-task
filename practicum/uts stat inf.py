import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data hasil pemilu
data = {
    'nama_partai': ['Partai Kebangkitan Bangsa', 'Partai Gerakan Indonesia Raya', 'Partai PDI Perjuangan', 'Partai Golkar', 'Partai Nasdem', 'Partai Buruh', 'Partai Gelombang Rakyat Indonesia', 'Partai Keadilan Sejahtera', 'Partai Kebangkitan Nusantara', 'Partai Hati Nurani Rakyat', 'Partai Garda Republik Indonesia', 'Partai Amanat Nasional', 'Partai Bulan Bintang', 'Partai Demokrat', 'Partai Solidaritas Indonesia', 'Partai Perindo', 'Partai Persatuan Pembangunan', 'Partai Ummat'],
    'suara_sah': [16115655, 20071708, 25387279, 23208654, 14660516, 972910, 1281991, 12781353, 326800, 1094588, 406883, 10984003, 484486, 11283160, 4260169, 1955154, 5878777, 642545]
}

# Membuat dataframe
df = pd.DataFrame(data)

# Membuat kelas-kelas
kelas_ganjil = np.arange(5000000, df['suara_sah'].max() + 5000000, 5000000)
kelas_genap = np.arange(2500000, df['suara_sah'].max() + 2500000, 2500000)

# Menghitung frekuensi
frekuensi_ganjil, _ = np.histogram(df['suara_sah'], bins=kelas_ganjil)
frekuensi_genap, _ = np.histogram(df['suara_sah'], bins=kelas_genap)

# Menambahkan kelas terakhir untuk mengakomodasi data yang melebihi batas atas
kelas_ganjil = np.append(kelas_ganjil, df['suara_sah'].max())
kelas_genap = np.append(kelas_genap, df['suara_sah'].max())

# Menambahkan kelas 0 untuk mengakomodasi data yang lebih kecil dari batas bawah
kelas_ganjil = np.insert(kelas_ganjil, 0, 0)
kelas_genap = np.insert(kelas_genap, 0, 0)

# Mencari nilai tengah masing-masing kelas
nilai_tengah_ganjil = (kelas_ganjil[:-1] + kelas_ganjil[1:]) / 2
nilai_tengah_genap = (kelas_genap[:-1] + kelas_genap[1:]) / 2

# Membuat histogram distribusi frekuensi
plt.figure(figsize=(12, 6))
plt.bar(nilai_tengah_ganjil, frekuensi_ganjil, width=4000000, align='center', alpha=0.7, label='NIM Ganjil')
plt.bar(nilai_tengah_genap, frekuensi_genap, width=2000000, align='center', alpha=0.7, label='NIM Genap')
plt.xlabel('Jumlah Suara')
plt.ylabel('Frekuensi')
plt.title('Histogram Distribusi Frekuensi Suara Partai Politik')
plt.legend()
plt.show()
