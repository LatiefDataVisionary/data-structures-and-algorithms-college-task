Algoritm Exchange Sort

Deklarasi
    x : aray [1..100] of real.
    Temp : real.
    i, n, j : integer.

Deskripsi
    input(n).
    ulang i=1 sampai n dengan melakukan input(x[i]).
    i <-- 1
    Selama i < n lakukan:
    {
        j <-- i + 1;
        selama j <= n lakukan:
        {
            Jika x[i] > x[j] maka 
            {
                Temp <-- x[i]
                x[i]  <-- x[j]
                x[j]  <-- temp
            }
            j  <-- j +1
        }
        i <--i + 1
    }
    ulang i=1 sampai n dengan melakukan output (x[i]).
