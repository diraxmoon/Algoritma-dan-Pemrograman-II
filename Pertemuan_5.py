#1. Comparison operator
x=0
y=1
z=1

print(x==y)
print(x==z)
print(x!=y)
print(x!=z)
print(x<y)
print(y<z)
print(x>y)
print(y>z)
print(x<=y)
print(x<=z)
print(y<=z)
print(x>=y)
print(x>=z)
print(y>=z)


#2. kuis 11
n = float(input())

if n < 100:
    print("false")

if n > 100:
    print("true")


#3. if tunggal
x = 8

if x == 8:
    print("x sama dengan 8")
    
    
#4. rangkaian if
x = 15

if x > 10:
    print("x lebih besar dari 10")

if x < 15:
    print("x lebih kecil dari 15")
    
if x == 15:
    print("x sama dengan 15")
    
    
#5. if-else
x = 10
if x < 10:
    print("x lebih kecil dari 10")
    
else:
    print("x lebih besar atau sama dengan 10")
    
    
#6. if-elif-else
x = 10
if x == 10:
    print("x == 10")

elif x > 15:
    print("x > 15")
    
elif x > 10:
    print("x > 10")
    
elif x > 5:
    print("x > 5")
    
else:
    print("x lebih kecil dari 5")
    
    
#7. membandingkan 2 angka input
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 > angka2:
    angka_besar = angka1
else: angka_besar = angka2    

print("Angka yang besar adalah ", angka_besar)


#8. kuis 12
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    angka_besar = angka1
elif angka2 > angka1 and angka2 > angka3:
    angka_besar = angka2
else:
    angka_besar = angka3

print("Angka yang besar adalah ", angka_besar)


#9. fungsi max()
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga :"))

angka_besar = max(angka1,angka2,angka3)

print("Angka paling besar adalah ", angka_besar)


#10. kuis 13
pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))

if pendapatan <= 60000000:
    pajak = pendapatan * 0.05
elif pendapatan <= 250000000:
    pajak = pendapatan * 0.15
elif pendapatan <= 500000000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30

print("Pajak penghasilan yang harus Anda bayar adalah ", pajak, "rupiah")