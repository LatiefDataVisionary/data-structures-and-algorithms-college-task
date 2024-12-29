def input_array(n):
    """
    Mengambil input dari pengguna untuk array x.
    """
    x = []
    for _ in range(n):
        x.append(int(input("Masukkan angka: ")))
    return x

def exchange_sort(x):
    """
    Mengurutkan array x menggunakan algoritma Exchange Sort.
    """
    n = len(x)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
                print(f"Pass {i+1}: {x}")  # Menampilkan hasil setiap langkah

def main():
    n = int(input("Masukkan panjang array: "))
    x = input_array(n)
    print("Urutan awal:")
    print(x)
    exchange_sort(x)
    print("Array setelah diurutkan:")
    print(x)

if __name__ == "__main__":
    main()
