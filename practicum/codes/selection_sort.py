def nginput_array(n):
    x = []
    for el in range(n):
        x.append(int(input(f"Masukkan angka ke-{el+1}: ")))
    return x

def proses_program(x):
    n = len(x)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if x[j] < x[min]:
                min = j
                # j = j + 1
        if min != i:
            temp = x[min]
            x[min] = x[i]
            x[i] = temp
            # x[i], x[min] = [min], x[i]
            print(f"Pass {i+1}: {x}")  
        
        i = i + 1

                
def main():
    n = int(input("Masukkan panjang array: "))
    x = nginput_array(n)
    print("Urutan awal:")
    print(x)
    print("\nProses program Selection Sort: ")
    proses_program(x)
    print("Array setelah diurutkan:")
    print(x)

main()

## Selection Sort
def ngo_nglebokke_arrayne():
    dowone_ongko = int(input("\nLebokno dowone array: "))
    ongko = []
    for el in range(dowone_ongko):
        ongko.append(int(input(f"Lebokno isine array ke-{el+1}: ")))
        # iwak = iwak + 1
    return ongko

def proses_kerjone(ongko):
    dowone_ongko = len(ongko)
    for kepisan in range(dowone_ongko - 1):
        cilik = kepisan
        for kepindo in range(kepisan+1, dowone_ongko):
            if ongko[kepindo] < ongko[cilik]:
                cilik = kepindo
        ongko[kepisan], ongko[cilik] = ongko[cilik], ongko[kepisan]
        # ongko[kepisan] = ongko[cilik]
        # ongko[cilik] = ongko[kepisan]
        print(f"Mubeng ke-{kepisan}: {ongko}")

def utomo():
    ongko = ngo_nglebokke_arrayne()
    print("\nArray awale koyoto ngene:")
    print(ongko)
    print("\nProses program Selection Sort: ")
    proses_kerjone(ongko)
    print(f"\nOngko sek bener: {ongko}\n")

if __name__ == "__main__":
    utomo()