#1
print("Tell me anything...")
anything = input()
print("Hmm...", anything,"...Really?")


#2
anything = input("Tell me anything...")
print("Hmm...", anything,"...Really?")





#4
anything = float (input("Enter a Number :"))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


#5
leg_a = float (input("input first leg length: "))
leg_b = float (input("input second leg length: "))
hypo = (leg_a ** 2 + leg_b **2)** .5
print("hypotenuse length is :", hypo)


#6
leg_a = float (input("input first leg length: "))
leg_b = float (input("input second leg length: "))
print("hypotenuse length is :", (leg_a ** 2 + leg_b **2)** .5)


#7
fname = input("May I have your first name, please?")
lname = input("May I have your last name, please?")
print("Thank you.")
print("\nYour name is " + fname + " " + lname + ".")


#8
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


#9
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


#10
x = input("Enter a number: ")
print(type(x))


#11
a = float(input("Enter a Number: "))
b = float(input("Enter a Number: "))
penjumlahan = (a + b)
pengurangan = (a - b)
pembagian = (a / b)
perkalian = (a * b)
print("a + b = ", penjumlahan)
print("a - b = ", pengurangan)
print("a / b = ", pembagian)
print("a * b = ", perkalian)
print("Selamat kamu sudah pintar matematika ^_^")


#12
x = float(input("Masukkan nilai x: "))
y = (1 / (x + 1 / (x + 1 / (x + 1 / x))))
print("y = (1 / (x + 1 / (x + 1 / (x + 1 / x))))")
print("Hasil dari variabel y adalah ", (1 / (x + 1 / (x + 1 / (x + 1 / x)))) )


#13
jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))
total_menit = menit + durasi
jam += total_menit // 60
menit = total_menit % 60
jam = jam % 24
print(f"Acara berakhir pukul {jam:02d}:{menit:02d}")