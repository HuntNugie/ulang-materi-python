# if statement merupakan kontrol alur program dimana kita dapat menjalankan program berdasarkan kondisi tertentu
# if statement ini akan menjalankan program jika kondisi tertentu true maka blok if nya akan di jalankan

# program mencari angka bulat dan genap
# print("=" * 5)
# inputan = int(input("Masukan angka  : "))

# # jika hanya satu statement
# # if inputan % 2 == 0 :
# #     print(f"{inputan} termasuk bilangan bulat")

# # jika 2 statement
# if inputan % 2 == 0 :
#     print(f"{inputan} termasuk bilangan bulat")
# else : 
#     print(f"{inputan} termasuk bilangan ganjil")
    
# program pengecekan usia untuk buat ktp

# jika lebih dari 2 statement
inputan = int(input("Masukan usia anda : "))

if inputan >= 17:
    print(f"usia anda {inputan} boleh membuat ktp")
elif inputan > 13 :
    print(f"usia anda {inputan} sedikit lagi boleh buat ktp")
else :
    print(f"usia anda {inputan} masih terlalu kecil untuk buat ktp")

