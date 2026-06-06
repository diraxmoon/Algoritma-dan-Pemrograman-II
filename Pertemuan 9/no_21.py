#Kuis 22
data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unik = []

for angka in data:
    if angka not in unik:
        unik.append(angka)

print("List asli :", data)
print("List unik :", unik)