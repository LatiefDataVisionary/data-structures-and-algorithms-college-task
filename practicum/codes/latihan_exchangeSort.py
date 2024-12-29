def exchange_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # Tukar elemen jika elemen pertama lebih besar dari elemen kedua
                arr[i], arr[j] = arr[j], arr[i]
                # Tampilkan proses tukar
                print(f"Swap: {arr[i]} <-> {arr[j]}")
            else:
                # Jika tidak ada pertukaran, tampilkan pesan
                print(f"No Swap: {arr[i]} <-> {arr[j]}")
    return arr

# Menerima inputan dari pengguna
arr = list(map(int, input("Masukkan daftar bilangan (pisahkan dengan spasi): ").split()))

# Menampilkan daftar sebelum diurutkan
print("Sebelum diurutkan:", arr)

# Mengurutkan daftar menggunakan Exchange Sort
sorted_arr = exchange_sort(arr)

# Menampilkan daftar setelah diurutkan
print("Setelah diurutkan:", sorted_arr)
