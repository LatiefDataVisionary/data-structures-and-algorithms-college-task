def exchange_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        print(f"Iterasi ke-{i+1}: {arr}")

def input_array():
    n = int(input("Masukkan panjang array: "))
    arr = []
    for i in range(n):
        x = int(input(f"Masukkan elemen ke-{i+1}: "))
        arr.append(x)
    return arr

def output_array(arr):
    print("Array setelah diurutkan:")
    for i in range(len(arr)):
        print(arr[i], end=" ")

def main():
    arr = input_array()
    print("Array sebelum diurutkan:", arr)
    exchange_sort(arr)
    output_array(arr)

if __name__ == "__main__":
    main()
