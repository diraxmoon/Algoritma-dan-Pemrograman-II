#no 5 kuis IMT
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

#kategorikan nilai imt yg sudah didapat
if index_massa_tubuh < 25:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[0])
elif index_massa_tubuh < 30:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[1])
else: print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[2], ".Anda harus diet!")