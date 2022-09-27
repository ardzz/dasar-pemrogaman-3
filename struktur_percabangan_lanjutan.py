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
