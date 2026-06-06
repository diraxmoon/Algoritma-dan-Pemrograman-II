#Menangani exception
while True:
    try:
        bilangan = int(input("Masukkan bilangan natural: "))
        print("Kebalikan dari ", bilangan, "adalah ", 1/bilangan)
        break
    except:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")