#Menangani multiple exception
while True:
    try:
        bilangan = int(input("Masukkan bilangan natural: "))
        print("Kebalikan dari ", bilangan, "adalah ", 1/bilangan)
        break
    except ValueError:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")
    except ZeroDivisionError:
        print("Peringatan! Tidak bisa membagi dengan 0")
    except:
        print("Maaf sepertinya ada yang salah nih... :(")