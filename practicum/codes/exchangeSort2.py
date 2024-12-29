def exchange_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # Pertukaran elemen
                arr[i], arr[j] = arr[j], arr[i]

def input_array():
    n = int(input("Masukkan panjang array bolo: "))
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
    exchange_sort(arr)
    output_array(arr)

# if __name__ == "__main__":
main()
