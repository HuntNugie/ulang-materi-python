# operator perbandingan
# operator yang bertugas membandingkan 2  buah nilai yang akan menghasilkan nilai boolean true or false

# == (sama dengan) -> akan bernilai true jika kedua nilainya sama
nilaiA = 10
nilaiB = 10
hasil = nilaiA == nilaiB
print(f"Hasil dari {nilaiA} apakah sama dengan {nilaiB} : {hasil}")

# !== (tidak sama dengan) -> akan bernilai true jika kedua nilainya tidak sama dengan
hasil = nilaiA != nilaiB
print(f"hasil dari {nilaiA} apakah tidak sama dengan nilai {nilaiB} : {hasil}")

# > (lebih besar dari) -> akan bernilai true jika nilai yang ada di sebalah kiri lebih besar dari nilai sebelah kanan
nilaiA = 10
nilaiB = 8
hasil = nilaiA > nilaiB
print(f"Hasil dari {nilaiA} apakah lebih besar dari {nilaiB} : {hasil}")

# >= (lebih besar dari atau sama dengan) -> akan bernilai true jika nilai yang ada di sebelah kiri lebih besar atau sama dengan nilai sebelah kanan
hasil = nilaiA >= nilaiB
print(f"Hasil dari {nilaiA} apakah lebih besar dari atau sama dengan {nilaiB} : {hasil}")

# < (lebih kecil dari) -> akan bernilai true jika nilai yang ada di sebelah kiri lebih kecil dari nilai sebelah kanan
nilaiA = 5
nilaiB = 10
hasil = nilaiA < nilaiB
print(f"Hasil dari {nilaiA} apakah lebih kecil dari {nilaiB} : {hasil}")

# <= (lebih kecil dari atau sama dengan) -> akan bernilai true jika nilai yang ada di sebelah kiri lebih kecil dari atau sama dengan nilai sebelah kanan
hasil = nilaiA <= nilaiB
print(f"Hasil dari {nilaiA} apakah lebih kecil dari atau sama dengan {nilaiB} : {hasil}")

