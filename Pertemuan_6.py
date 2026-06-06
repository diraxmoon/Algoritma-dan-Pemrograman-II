#1
#contoh 1
while True:
    print("nyangkut di perulangan tak hingga")


#2
#contoh 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1


#3
#membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0

#membaca angka pertama
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

while angka != 0: #cek apakah angka tidak sama dengan 0
    if angka % 2 == 1: #mengecek apakah sisa bagi angka dengan 2 adalah 1
        angka_ganjil += 1
    else:
        angka_genap += 1
        
    #membaca angka selanjutnya
    angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

#menampilkan total angka ganjil dan angka genap
print("Jumlah Angka Ganjil: ", angka_ganjil)
print("Jumlah Angka Genap: ", angka_genap)


#4 (kuis 15)
secret_number = 777

print(
"""

+========================================+
| Selamat datang di game saya, muggle!   |
| masukkan suatu angka dan tebak         |
| angka berapa yang saya pilih           |
| untuk kamu.                            |
| Jadi, berapa angka rahasianya?         |
+========================================+
""")

# meminta user memasukkan angka pertama
tebakan = int(input("Masukkan angka tebakanmu: "))

# perulangan while selama tebakan salah
while tebakan != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    tebakan = int(input("Masukkan angka lagi: "))

# jika tebakan benar
print("Selamat, Muggle! kamu bebas sekarang!")


#5
for a in range(10):
    print("nilai a saat ini adalah", a)

for b in range(2,8):
    print("nilai b saat ini adalah", b)

for c in range(2,8,3):
    print("nilai c saat ini adalah", c)

for d in range(1,1):
    print("nilai d saat ini adalah", d)

for e in range(2,1):
    print("nilai e saat ini adalah", e)


#6
power = 1
for expo in range(11):
    print ("2 pangkat ", expo, " adalah ", power)
    power *= 2


#7
#contoh break
print("Instruksi break: ")
for i in range(1,6):
    if i == 3:
        break
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")

#contoh continue
print("\nInstruksi continue: ")
for i in range(1,6):
    if i == 3:
        continue
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")


#8
# angka rahasia pesulap
secret_number = 7

print(
"""

+========================================+
| Selamat datang di game saya, muggle!   |
| masukkan suatu angka dan tebak         |
| angka berapa yang saya pilih           |
| untuk kamu.                            |
| Jadi, berapa angka rahasianya?         |
+========================================+
""")


while True:
    tebakan = int(input("Masukkan angka tebakanmu: "))

    if tebakan == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha! kamu nyangkut deh di Loop saya")



#9
# meminta user memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ").upper()
user_word = kata

# perulangan untuk setiap huruf
for kata in user_word:
    if kata == "A" or kata == "I" or kata == "U" or kata == "E" or kata == "O":
        continue
    elif user_word:
        print(kata)
    else:
        print("Karakter bukan huruf")


#10
#perulangan while dengan else
i = 1
while i < 5:
    print(i)
    i += 1
    
else:
    print("else:", i)


#11
#perulangan for dengan else
for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2,1):
    print(i)
else:
    print("else:", i)


#12
#ekspresi logika
i = 1
j = not not i

print(j)


#13
#operasi logical vs. bit
i = 15
j = 22

log = i and j
print(log)

bit = i & j
print(bit)

logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)


#14
#binary shifting
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)


#15

#operator bitwise
# &(ampersand) - bitwise conjunction
# |(bar) - bitwise disjunctiion
# ~(tilde) - bitwise negation
# ^(caret) - bitwise exclusive or (xor)

x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)