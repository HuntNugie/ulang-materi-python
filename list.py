# list merupakan data strukture dimana kita dapat mneyimpan lebih dari satu data yang berbeda tipe mungkin jika di bahasa pemograman lain bisa di sebut array
# membuat list
daftar_kosong = []
print(daftar_kosong)
# di isi integer
angka = [1,2,3,4,5]
print(angka)
# di isi string
string = ["Nugie","Nadin","alexander"]
print(string)
# campuran
campuran = ["Nugie",21,"riany",20,"nadin",14]
print(campuran)


# mendapatkan satu data list
print(string[0]) # di ambil dengan menggunakan index

# menambahkan data baru

# menggunakna method append(akan menambahkan ke yang terbaru di akhir)
string.append("alexandria")
print(string)

# menggunakan method insert untuk custom dimana mau di tambahkan
string.insert(0,"Laurin") # ini custom mau dimana di tambahkan disini di set 0 jadi akan di tambahkan di paling pertama dan tidak akan di ganti data yang pertama
print(string)

# mengubah data
string[0] = "renayla" # ini akan mengganti index ke 0
print(string)

# menghapus data
string.remove("renayla") # ini akan menghapus data yang di pilih
print(string)

string.pop() # ini akan menghapus index terbaru/terakhir jika parameter nya tidak di isi
print(string)

campuran.pop(2) # jika di isi maka akan menghapus sesuai dengan nomor index nya
print(campuran)

# melooping list untuk mendapatkan isi value nya
for i in string:
    print(i)

i = 0
while i < len(campuran):
    print(campuran[i])
    i+=1

# menambahkan antar 2 list
gabungan = angka + string
print(gabungan)
