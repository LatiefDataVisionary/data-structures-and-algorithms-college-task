def nginput_array(n):
    x = []
    for el in range(n):
        x.append(int(input(f"Masukkan angka ke-{el+1}: ")))
    return x

def proses_program(x):
    n = len(x)
    if n <= 1:
        return

    for i in range (1, n):
        temp = x[i]
        j = i - 1
        while j >= 0 and temp < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = temp
        print(f"Pass {i}: {x}")  

                
def main():
    n = int(input("\nMasukkan panjang array: "))
    x = nginput_array(n)
    print("\nUrutan awal:")
    print(x)
    print("\nProses program Insertion Sort: ")
    proses_program(x)
    print("\nArray setelah diurutkan:")
    print(x)

if __name__ == "__main__":
    main()
    print("\n")
