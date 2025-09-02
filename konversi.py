# konversi atau kadang di sebut dengan casting merupakan merubah tipe data menjadi tipe data yang lain

# int()
# untuk mengkonversi ke int (hanya berlaku jika nilai nya itu adalah angka)
uang = 21.005
uang = int(uang)
print(uang)

# float()
# untuk mengkonversi ke float (hanya berlaku jika nilai nya itu adalah angka)
umur = 21
umur = float(umur)
print(umur)

# str()
# untuk mengkonversi ke string
is_married = True
print("Apakah Nugie sudah nikah ? ",str(is_married))

# bool()
# untuk mengkonversi ke boolean(jika nilai angka selain 0 nilainya True, untuk nilai string selain string kosong nilai nya True)
data = ""
data = bool(data)
print(data)
print(type(data))

