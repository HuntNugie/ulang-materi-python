# operator logika merupakan operator yang membandingkan dua buah boolean dan akan menghasilkan nilai boolean kembali

# and -> akan menghasilkan true jika kedua nya itu true
nilaiA = True
nilaiB = True
hasil = nilaiA and nilaiB
print(f"Hasil jika true and true adalah {hasil}")

# or -> akan menghasilkan true jika minimal salah satu nya true ataupun keduanya true
nilaiA = True
nilaiB = False
hasil = nilaiA or nilaiB
print(f"Hasil jika true or false adalah {hasil}")

# not -> akan membalikan nilai boolean yang asalnya true menjadi false dan sebaliknya
hasil = not nilaiA
print(f"Hasil dari kebalikan true adalah {hasil}")