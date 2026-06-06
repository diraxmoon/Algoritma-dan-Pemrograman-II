#Return tanpa ekspresi: memanggil fungsi dengan argumen False
def selamat_ulang_tahun(harapan=True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")
    if not harapan:
        return

    print("Selamat Ulang Tahun")

selamat_ulang_tahun(False)