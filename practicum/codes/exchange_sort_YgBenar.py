def nginput_array(n):
    x = []
    for el in range(n):
        x.append(int(input(f"Masukkan angka ke {el+1}: ")))
        el+=1
    return x

def proses_program(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                tem = x[i]
                x[i] = x[j]
                x[j] = tem
                # x[i], x[j] = x[j], x[i]
                print(f"Pass {i+1}: {x}")  
                
def main():
    n = int(input("Masukkan panjang array: "))
    x = nginput_array(n)
    print("Urutan awal:")
    print(x)
    proses_program(x)
    print("Array setelah diurutkan:")
    print(x)

if __name__ == "__main__":
    main()
