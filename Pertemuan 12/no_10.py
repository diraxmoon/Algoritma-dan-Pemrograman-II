#no 10
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    hasil_jumlah = 0 #untuk menampung hasil dari penjumlahan 2 elemen
    for i in range(n - 2):
        hasil_jumlah = elem_1 + elem_2
        elem_1 = elem_2
        elem_2 = hasil_jumlah

    return hasil_jumlah

for i in range(1,10):
    print(i, "->", fibonacci(i))