# match case merupakan kontrol alur program alternatif selain if statement dimana kita dapat mencocokan expression dengan value dari case nya, untuk match case ini tidak bisa melakukan perbandingan(bisa hanya saja dengan guard condition) karna match case ini hanya untuk mencocokan expression yang nilai nya sudah pasti

hari = input("Masukan nama hari : ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
        print("itu adalah hari anda belajar")
    case "sabtu" | "minggu" :
        print("hari tersebut opsional bisa libur bisa belajar")
    case _:
        print("Maaf yang anda masukan bukan lah nama hari")
        