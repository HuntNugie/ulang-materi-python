# looping berfungsi untuk mengulang ngulang program yang sama sesuai kondisi tertentu sehingga bisa berhenti

# for loop // secara defaul dimulai dari 0
for i in range(3) :
    print("Hello world")
    
# kalau tidak mau mulai dari 0, tetapi di index untuk stop nya akan berhenti 1 nomor karna sebenernya di belakang layar masih di hitung di mulai dari 0
for i in range(1,10):
    print(i)
    
print("="*10)
# kalau mau lewat
for i in range(1,15,3):
    print(i)
print("="*10)
# kalau mau terbalik
for i in range(10,-1,-1):
    print(i)