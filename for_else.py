# di dalam for kita dapat menggunakan else jadi kode else akan di jalankan jika looping for sudah berhasil selesai secara normal bukan dengan break


# program tebak angka
angka_rahasia = 9
for i in range(1,4):
    user = int(input("Masukan angka anda : "))
    if user == angka_rahasia:
        print(f"anda berhasil menabak angka {user}")
        break
    print("anda salah")
else:
    print("Batas kesempatan 3 kali anda sudah habis")