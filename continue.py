# continue berfungsi untuk melanjutkan iterasi sehingga jika masih ada kode di bawah continue tidak akan di eksekusi dan akan menjalankan iterasi selanjutnya

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(f"{i} bilangan ganjil")

# program ngecek angka ganjil mau dari mana sampai mana

print("Selamat datang di pengecekan angka ganjil dan genap")
pilih = input("Masukan anda mau ganjil atau genap : ")

if pilih.lower() == "genap":
    awal = int(input("mau mulai dari angka mana : "))
    akhir = int(input("Mau akhir di angka mana : "))
    for i in range(awal,akhir+1):
        if awal > akhir:
            break
        if i % 2 == 1:
            continue
        print(f"{i} - bilangan genap")
elif pilih.lower() == "ganjil":
    awal = int(input("mau mulai dari angka mana : "))
    akhir = int(input("Mau akhir di angka mana : "))
    for i in range(awal,akhir+1):
        if awal > akhir:
            break
        if i % 2 == 0:
            continue
        print(f"{i} - bilangan ganjil")
else :
    print("Mohon masukan dengan benar")