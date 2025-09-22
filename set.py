# set merupakan structure data yang berisi data yang tidak bisa duplikat dan tidak mempunyai index ataupun key serta tidak berurutan
data = {"Nugie kurniawan","Nadin nugraha","Ujang rusliandi"}

# menambahkan add
data.add("raka sagraha")

# menghapus
data.remove("Ujang rusliandi")

# mengupdate -> disini hanya bisa mengupdate iterable
data.update(("melinda","nazwa","natasya"))
print(data)

# mendapatkan data dengan looping
for dat in data:
    print(dat)