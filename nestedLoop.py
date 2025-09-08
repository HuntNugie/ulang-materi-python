# di dalam looping kita dapat looping bersarang jadi looping di dalma looping

# pilih perkalian 1-10 dan dapat memilih perkalian nya mau sampe perkalian berapa
awal = int(input("Masukan mau perkalian nya 1-berapa : "))
akhir = int(input("Mau dikali nya sampai kali berapa : "))

for i in range(1,awal+1):
    print("="*8)
    for j in range(1,akhir+1):
        print(f"{i} * {j} = {i*j}")
    print("="*8)
else:
    print("terimakasih telah berjuang")