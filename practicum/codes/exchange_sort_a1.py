def exchange_sort(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

def main():
    n = int(input("Masukkan panjang array: "))
    x = []
    for i in range(n):
        x.append(float(input(f"Masukkan angka ke {i+1}: ")))

    print("Urutan awal:")
    print(x)

    sorted_array = exchange_sort(x)

    print("Array setelah diurutkan:")
    for num in sorted_array:
        print(num)

if __name__ == "__main__":
    main()
