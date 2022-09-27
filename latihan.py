# input nama, nim, jurusan, dan nilai raport
nama = input("Masukkan nama: ")
nim = input("Masukkan nim: ")
jurusan = input("Masukkan jurusan: ")

# input nilai mata pelajaran ujian SMA
nilai_bahasa_indonesia = int(input("Masukkan nilai ahasa Indonesia: "))
nilai_bahasa_inggris = int(input("Masukkan nilai bahasa Inggris: "))
nilai_matematika = int(input("Masukkan nilai matematika: "))
nilai_fisika = int(input("Masukkan nilai fisika: "))
nilai_kimia = int(input("Masukkan nilai kimia: "))
nilai_biologi = int(input("Masukkan nilai biologi: "))

# hitung rata-rata nilai raport
rata_rata_nilai_raport = (nilai_bahasa_indonesia + nilai_bahasa_inggris + nilai_matematika + nilai_fisika + nilai_kimia + nilai_biologi) / 6

# cek apakah rata-rata nilai raport lebih dari 95
if rata_rata_nilai_raport > 95:
    # jika ya, maka tampilkan pesan
    print("Mahasiswa layak mendapatkan beasiswa kelas unggulan")
# cek apakah rata-rata nilai raport lebih dari 90
elif rata_rata_nilai_raport > 90:
    # jika ya, maka tampilkan pesan
    print("Mahasiswa layak mendapatkan beasiswa kelas regular")
# jika tidak, maka tampilkan pesan
else:
    print("Mahasiswa tidak layak mendapatkan beasiswa")