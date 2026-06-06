# ==============================
# PROGRAM SISTEM KASIR MINI
# ==============================

# Fungsi 1: Input Barang
def input_barang():
    daftar_barang = []
    jumlah = int(input("Masukkan jumlah barang: "))
    
    for i in range(jumlah):
        print(f"\nBarang ke-{i+1}")
        nama = input("Nama barang: ")
        harga = int(input("Harga barang: "))
        qty = int(input("Jumlah beli: "))
        
        daftar_barang.append({
            "nama": nama,
            "harga": harga,
            "qty": qty
        })
    
    return daftar_barang


# Fungsi 2: Hitung Total & Diskon
def hitung_total(daftar_barang):
    total = 0
    
    for barang in daftar_barang:
        subtotal = barang["harga"] * barang["qty"]
        total += subtotal
    
    # Diskon 10% jika total > 100000
    if total > 100000:
        diskon = total * 0.1
    else:
        diskon = 0
    
    total_bayar = total - diskon
    
    return total, diskon, total_bayar


# Fungsi 3: Tampilkan Struk
def tampilkan_struk(daftar_barang, total, diskon, total_bayar):
    print("\n===== STRUK BELANJA =====")
    
    for barang in daftar_barang:
        subtotal = barang["harga"] * barang["qty"]
        print(f"{barang['nama']} x{barang['qty']} = {subtotal}")
    
    print("------------------------")
    print(f"Total       : {total}")
    print(f"Diskon      : {diskon}")
    print(f"Total Bayar : {total_bayar}")
    print("========================")


# ==============================
# PROGRAM UTAMA
# ==============================
barang = input_barang()
total, diskon, total_bayar = hitung_total(barang)
tampilkan_struk(barang, total, diskon, total_bayar)