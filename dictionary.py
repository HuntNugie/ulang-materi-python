# dictionary merupakan data structure jika di bandingkan dengna bahasa pemograman yang lain itu mirip dengan object yang merupakan pasangan antara key dan value
mahasiswa = {
    "nama":"Nugie kurniawan",
    "prodi":"teknik informatika"
}
# cara memanggil
print(mahasiswa["nama"])

# cara menambahkan
mahasiswa["univ"] = "Stmik mardira"

# cara mengganti
mahasiswa["prodi"] = "IT"

# cara menghapus
mahasiswa.pop("univ")

# mendapatkan panjang dictionary
print(len(mahasiswa))

# dengan looping akan mengembalikan key nya saja
for key in mahasiswa:
    print(key)

# mendapatkan langsung dengan key dan value
for key,value in mahasiswa.items():
    print(key,value) 

print(mahasiswa.items())