# import library sqlite3
import sqlite3


# fungsi tambah data
def tambah_mahasiswa():
    # buat variabel untuk menyimpan biodata mahasiswa-mahasiswa
    mahasiswa = []

    # input biodata mahasiswa
    # input nama
    nama = input("Masukkan nama: ")

    # input nim
    nim = input("Masukkan nim: ")

    # input jurusan
    jurusan = input("Masukkan jurusan: ")

    # input angkatan
    angkatan = input("Masukkan angkatan: ")

    # tambahkan biodata mahasiswa ke dalam variabel mahasiswa
    mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "jurusan": jurusan,
        "angkatan": angkatan
    })

    # simpan data-data mahasiswa ke database sqlite
    # buka koneksi ke database
    database_mahasiswa = sqlite3.connect("mahasiswa.db")
    # buat tabel mahasiswa, jika belum ada maka buat, jika sudah ada maka abaikan
    database_mahasiswa.execute(
        "CREATE TABLE IF NOT EXISTS mahasiswa (nama TEXT, nim TEXT, jurusan TEXT, angkatan TEXT)")
    # simpan data mahasiswa ke database
    database_mahasiswa.execute("INSERT INTO mahasiswa VALUES (?, ?, ?, ?)", (nama, nim, jurusan, angkatan))
    # simpan perubahan
    database_mahasiswa.commit()
    # tutup koneksi ke database
    database_mahasiswa.close()
    # tampilkan pesan
    print('Data berhasil disimpan')


# fungsi hapus data
def hapus_mahasiswa():
    # input nim mahasiswa yang akan dihapus
    nim = input("Masukkan nim: ")

    # hapus data mahasiswa dari database
    # buka koneksi ke database
    database_mahasiswa = sqlite3.connect("mahasiswa.db")
    # hapus data mahasiswa dari database
    database_mahasiswa.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
    # cek apakah data sudah terhapus
    if database_mahasiswa.total_changes > 0:
        # simpan perubahan
        database_mahasiswa.commit()
        # tampilkan pesan
        print("Data berhasil dihapus")
    # jika tidak, maka tampilkan pesan
    else:
        print("Data tidak ditemukan")
    # tutup koneksi ke database
    database_mahasiswa.close()


# fungsi tampilkan data
def tampilkan_mahasiswa():
    # buka koneksi ke database
    database_mahasiswa = sqlite3.connect("mahasiswa.db")
    # ambil data mahasiswa dari database
    data_mahasiswa = database_mahasiswa.execute("SELECT * FROM mahasiswa")
    # tampilkan data mahasiswa dengan tabel
    print("Nama\tNIM\tJurusan\tAngkatan")
    # tampilkan data mahasiswa
    for mahasiswa in data_mahasiswa:
        print(f"{mahasiswa[0]}\t{mahasiswa[1]}\t{mahasiswa[2]}\t{mahasiswa[3]}")
    # tutup koneksi ke database
    database_mahasiswa.close()


# fungsi menu
def menu():
    # tampilkan menu dengan perulangan tak hingga
    while True:
        # tampilkan menu
        print("Menu:")
        print("1. Tambah data mahasiswa")
        print("2. Hapus data mahasiswa")
        print("3. Tampilkan data mahasiswa")
        print("4. Keluar")
        # input pilihan menu
        pilihan = input("Masukkan pilihan: ")

        # cek apakah pilihan menu adalah 1
        if pilihan == "1":
            # jika ya, maka jalankan fungsi tambah_mahasiswa()
            tambah_mahasiswa()

        # cek apakah pilihan menu adalah 2
        elif pilihan == "2":
            # jika ya, maka jalankan fungsi hapus_mahasiswa()
            hapus_mahasiswa()

        # cek apakah pilihan menu adalah 3
        elif pilihan == "3":
            # jika ya, maka jalankan fungsi tampilkan_mahasiswa()
            tampilkan_mahasiswa()

        # cek apakah pilihan menu adalah 4
        elif pilihan == "4":
            # jika ya, maka keluar dari perulangan
            break

        # jika tidak, maka tampilkan pesan
        else:
            print("Pilihan tidak ditemukan")


# jalankan fungsi menu
menu()