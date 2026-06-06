#Kuis 25
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def hari_pada_tahun(tahun, bulan, hari):
    jumlah_hari = hari

    for b in range(1, bulan):
        jumlah_hari += hari_didalam_bulan(tahun, b)

    return jumlah_hari

print(hari_pada_tahun(2000, 12, 31))