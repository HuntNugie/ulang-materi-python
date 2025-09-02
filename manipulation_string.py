# manipulation string

# menyambung string
# menggunakan tanda plus
nama_depan = "nugie"
nama_belakang = "kurniawan"
nama_lengkap = nama_depan+ " "+nama_belakang
print(nama_lengkap)

# len()
# menghitung panjang string
print(len(nama_lengkap))

# indexing
# dalam python kita dapat mendapatkan karakter karakter dalam 1 teks string
bahasa = "python"
# dimulai dengan 0
print(bahasa[0])
print(bahasa[1])
print(bahasa[2])

# jika ingin mendapatkan nilai langsung yang belakang kita bisa menggunakan dengan minus -1
print(bahasa[-1])
print(bahasa[-2])
print(bahasa[-3])

# kita bisa mendapatkan string dengan range
bahasa = "javascript"
print(bahasa[0:3]) #index awal itu di dimana karakter dimulai dan index akhir itu dimana karakter sebelum di akhiri jadi index akhir tidak akan di ambil
print(bahasa[:4]) #jika kita tidak set index awal maka akan menggunakan default nya itu 0
print(bahasa[4:]) #jika kita tidak set index akhir nya maka akan menggunakan di mulai dari index awal dan sampai paling akhir

# menggunakan method string
# ada banyak method string 

# capitalize()
# berfungsi untuk agar karakter depan nya itu akan menjadi besar
nama = "nugie"
print(nama.capitalize())

# upper
# akan berfungsi untuk agar semua karakter menjadi besar
print(nama.upper())

# lower
# berfungsi untuk agar semua karakter menjadi kecil semua
nama = "NUGIE KURNIAWAN"
print(nama.lower())

# title
# berfungsi untuk agar semua kalimat di awali dengan huruf besar
judul = "you are the apple of my eye"
print(judul.title())

# strip
# berfungsi untuk menghilangkan karakter tertentu dalam string
nama = "Nugie kurniawan"
print(nama.strip("kurniawan"))

# split berfungsi untuk memisahkan dan menjadikan dalam bentuk array
print(nama.split())

# count
# berfungsi untuk mendapatkan berapa banyak karakter
print(nama.count("n"))

# method method untuk mengecek akan mengembalikan true or false

# isalpha
# berfungsi untuk mengecek apakah seluruhnya itu alphabet semua tidak ada string 
nama = "nugie"
print(nama.isalpha())

# isalnum
# berfungsi unutk mengecek apakah terdapat kombinasi antara alphabet dan numeric number
nama = "nugie123"
print(nama.isalnum())

# isdecimal
umur = "123123"
print(umur.isdecimal())

judul = "You Are The Apple Of My Eye"
print(judul.istitle())

# escape karakter

# \t -> untuk tab
print("Nugie \t\tkurniawan")

# \n -> untuk newline
print("Nama : Nugie kurniawan \nUmur : 21")

# multiline
print("""
Nugie kurniawan
teknik informatika
laki laki      
      """)

# mendapatkan backslash menjadi string
print("C\\User\\Nugie")

# format string
# kita tidak perlu menggunakan concat(+) untuk menghubungkan string satu dengan yang lainnya
nama_depan = "Nugie"
nama_belakang = "kurniawan"
nama_lengkap = f"nama lengkap = {nama_depan} {nama_belakang}"
print(nama_lengkap)

# dalam format string kita bisa menambahkan expression(code yang menghasilkan hasil)
a = 500
b = 4
print(f"hasil = {a*b:,}") #pakai :, untuk otomatis menjadi ada koma untuk angka ribuan ke atas

# mendapatkan beberapa angka di belakang .
decimal = 21.324645
print(f"hasil {decimal:.2f}")

