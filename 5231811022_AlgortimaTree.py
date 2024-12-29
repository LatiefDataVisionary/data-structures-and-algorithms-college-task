print("="*4+"5231811022_AlgoritmaTree"+"="*4+"\n")

def algoritma_tree_p14(n):
    #logicnya
    for i in range(1, n):
        anak_kiri = 2 * i
        anak_kanan = 2 * i + 1
        
        if anak_kiri <= n:
            print(f"\t{i} \t---> {anak_kiri}")
        if anak_kanan <= n:
            print(f"\t{i} \t---> {anak_kanan}")

# Minta input angka utk menentukan hingga angka berapa struktur pohon akan dibuat
print("- Misal 15(seperti yg dipapan)")
angka_tertinggi = int(input("Mau sampai angka berapa? : "))
print("  Ortu angka\tAnak angka")
algoritma_tree_p14(angka_tertinggi)
print()