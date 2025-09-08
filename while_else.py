# while juga mempunyai else, kode else akan di jalankan jika while berhenti secara normal bukan dengan break
# program masukan password dengan kesempatan
password = ""
password_correct = "nugietea123"
kesempatan = 3
while kesempatan > 0:
    password = input("Masukan password anda : ")
    if password == password_correct :
        print(f"Password anda sudah benar : {password}")
        break
    kesempatan -= 1
    print(f"Password anda salah, sisa {kesempatan} kesempatan lagi")
else:
    print("kesempatan anda sudah habis, akses ditolak")
    