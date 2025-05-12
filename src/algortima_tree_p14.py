# def piramida_angka(panjang_baris):
#     # Determine the maximum number to be printed
#     max_number = sum(range(1, panjang_baris + 1))
    
#     # Calculate the width of the widest number
#     panjang_kolom = len(str(max_number)) + 1
    
#     angka_terbaru = 1

#     for row in range(1, panjang_baris + 1):
#         # Calculate the number of leading spaces
#         leading_spaces = ' ' * (2 ** (panjang_baris - row) - 1) * (panjang_kolom // 2)
#         print(leading_spaces, end='')
        
#         for col in range(1, row + 1):
#             print(f"{angka_terbaru:<{panjang_kolom}}", end='')
#             angka_terbaru += 1
            
#             if col < row:
#                 spaces_between = ' ' * (2 ** (panjang_baris - row + 1) - 1) * panjang_kolom
#                 print(spaces_between, end='')
        
#         # Move to the next line
#         print()

# # Test the function with 4 rows to see the numbers up to 15
# piramida_angka(4)




def algoritma_tree_p14(n):
    for i in range(1, n):
        anak_kiri = 2 * i
        anak_kanan = 2 * i + 1
        
        if anak_kiri <= n:
            print(f"{i} ---> {anak_kiri}")
        if anak_kanan <= n:
            print(f"{i} ---> {anak_kanan}")

# Minta input dari pengguna untuk menentukan hingga angka berapa struktur pohon akan dibuat
angka_tertinggi = int(input("Mau sampai angka berapa? : "))
algoritma_tree_p14(angka_tertinggi)
