# break berfungsi untuk memberhenti kan looping yang sedang berjalan jadi istilah berhentikan secara paksa
# berhenti = 12
# angka = 1
# while angka < 20:
#     print(angka)
#     if(angka == berhenti):
#         break
#     angka += 1
    

# membuat program password
user = ""
password = "nugitea123"

while user != password:
    user = input("Masukan password anda : ")
    if user == password:
        print(f"Password anda benar = {user}")
        break
    print("Password anda salah")