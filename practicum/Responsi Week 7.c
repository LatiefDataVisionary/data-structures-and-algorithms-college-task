#include <stdio.h>

int main() {
    int array[5];
    int i, angka;
    int temu = 0; // variabel flag utk menandai apakah angka ditemukan atau tdk

    printf("Masukkan 5 elemen untuk array:\n");

    // Memasukkan input dari pengguna ke dlm array
    for (i = 0; i < 5; i++) {
        printf("Masukkan nilai ke-%d: ", i + 1);
        scanf("%d", &array[i]);
    }

    printf("\nMasukkan angka yg dicari: ");
    scanf("%d", &angka);

    // Memeriksa apakah angka yg dicari ada di dlm array
    for (i = 0; i < 5; i++) {
        if (array[i] == angka) {
            temu = 1; // set flag menjadi 1 jika angka ditemukan
            break;
        }
    }

    // Menampilkan pesan sesuai dg hasil pencarian
    if (temu) {
        printf("%d ada di dalam program.\n", angka);
    } else {
        printf("%d tidak ada di dalam program.\n", angka);
    }

    return 0;
}

