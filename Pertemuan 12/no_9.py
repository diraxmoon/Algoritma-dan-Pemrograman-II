#no 9
def faktorial(n):
    #bilangan yang akan difaktorial harus lebih besar dari 0
    if n < 0:
        return None
    
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1

    hasil = 1
    for i in range (2, n + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorialkan: "))
print(n,"! = ", faktorial(n))