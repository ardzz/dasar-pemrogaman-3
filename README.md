### JOBSHEET 3 - DASAR PEMROGRAMMAN
<p align="center">
    <img src="https://github.com/ardzz/dasar-pemrogaman-2/raw/master/images/logo-polines.png" alt="Logo Polines" width="300" height="300">
</p>

#### Dibuat dan disusun oleh
| Variabel | Nilai               |
|----------|---------------------|
| Nama     | Naufal Reky Ardhana |
| NIM      | 4.33.22.0.21        |
| Kelas    | TI-1A               |

**PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK ELEKTRO POLITEKNIK NEGERI SEMARANG - 2022**

#### Tujuan Praktikum
- Mahasiswa mampu memahami dan menerapkan konsep dasar pemrograman
- Mahasiswa dapat menggunakan perintah struktur kontrol Python
- Mahasiswa dapat menggunakan perintah perulangan Python

#### Alat dan Bahan
- Laptop
- Python `3.10.0`
- PyCharm `2020.3.3`
- Git `2.30.0`

<br>

#### BAB 1 - Dasar Teori

##### Struktur Kontrol
Struktur kontrol adalah suatu perintah yang digunakan untuk mengatur alur program. Struktur kontrol terdiri dari dua jenis, yaitu struktur kontrol perulangan dan struktur kontrol percabangan.
##### 1.2. Struktur Percabangan
Struktur kontrol percabangan adalah suatu perintah yang digunakan untuk mengatur alur program berdasarkan kondisi tertentu. Struktur kontrol percabangan terdiri dari dua jenis, yaitu struktur kontrol percabangan `if` dan struktur kontrol percabangan `if-else`.
##### 1.3. Struktur Perulangan
Struktur perulangan adalah suatu perintah yang digunakan untuk mengulang suatu perintah tertentu. Struktur perulangan terdiri dari dua jenis, yaitu struktur perulangan `for` dan struktur perulangan `while`.

<br>

#### BAB 2 - Praktikum
##### 2.1. Struktur Percabangan
###### 2.1.1. Struktur Percabangan `if-else`
```python
# input umur
umur = int(input("Masukkan umur: "))

# input minimal umur
minimal_umur = 18

# cek apakah umur lebih besar atau sama dengan minimal umur
if umur >= minimal_umur:
    
    # jika ya, maka tampilkan pesan
    print("Anda sudah cukup umur untuk membuat SIM")
    
# jika tidak, maka tampilkan pesan
else:
    print("Anda belum cukup umur untuk membuat SIM")
```


###### 2.1.2. Struktur Perulangan
```python
# membuat segitiga terbalik
# gunakan reversed() untuk membalikkan angka
for i in reversed(range(1, 10)):
    
    # cetak karakter * sebanyak i
    print("*" * i)
```


###### 2.2.3 Struktur Percabangan Lanjutan
```python
# program pembandingan 3 bilangan
# input bilangan 1
bilangan_1 = int(input("Masukkan bilangan 1: "))

# input bilangan 2
bilangan_2 = int(input("Masukkan bilangan 2: "))

# input bilangan 3
bilangan_3 = int(input("Masukkan bilangan 3: "))

# cek apakah bilangan 1 lebih besar dari bilangan 2
if bilangan_1 > bilangan_2:
    
    # jika ya, maka cek apakah bilangan 1 lebih besar dari bilangan 3
    if bilangan_1 > bilangan_3:
        
        # jika ya, maka tampilkan bilangan 1
        print(f"Bilangan 1 ({bilangan_1}) lebih besar dari bilangan 2 ({bilangan_2}) dan bilangan 3 ({bilangan_3})")
    
    # jika tidak, maka tampilkan bilangan 3
    else:
        print(f"Bilangan 3 ({bilangan_3}) lebih besar dari bilangan 1 ({bilangan_1}) dan bilangan 2 ({bilangan_2})")

# jika tidak, maka cek apakah bilangan 2 lebih besar dari bilangan 3
elif bilangan_2 > bilangan_3:
    
    # jika ya, maka tampilkan bilangan 2
    print(f"Bilangan 2 ({bilangan_2}) lebih besar dari bilangan 1 ({bilangan_1}) dan bilangan 3 ({bilangan_3})")

# jika tidak, maka tampilkan bilangan 3
else:
    print(f"Bilangan 3 ({bilangan_3}) lebih besar dari bilangan 1 ({bilangan_1}) dan bilangan 2 ({bilangan_2})")

```