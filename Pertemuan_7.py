#NO_1
angka = [1, 2, 3, 4, 5]
print("isi dari list awal:", angka) #printing isi dari list awal

angka[3] = 6
print("isi dari list baru: ", angka) #isi dari list yang sudah diubah


#NO_2
angka = [1, 2, 3, 6, 5]
print("\n", angka[1]) #mengakses elemen kedua pada list

#NO_3
print("\nPanjang list: ", len(angka)) #print panjang dari list

#NO_4
angka = [1, 2, 3, 6, 5]
del angka[1]
print("\n", len(angka))
print(angka)

#NO_5
numbers = [1, 3, 6, 5]
print("\n", numbers[-2])

#NO_6_kuis_19
topi_list = [1, 2, 3, 4, 5] #angka yang tersembunyi di dalam topi pesulap

#Langkah 1: tulis satu baris kode yang meminta user memasukkan angka integer
#untuk di-replace ke nilai tengah dari list
topi_list[2] = 7

#Langkah 2: tulis satu baris kode untuk menghapus elemen terakhir pada list
topi_list = [1, 2, 7, 4, 5]
del topi_list[4]

#Langkah 3: tulis satu baris kode untuk menampilkan panjang dari list
print("\nPanjang list: ", len(angka))

print(topi_list)

#NO_7_contoh_1
angka = [1, 3, 6, 5]
print("\n", len(angka))
print(angka)

###

angka.append(7)

print(len(angka))
print(angka)

###

angka.insert(1, 333)
print(len(angka))
print(angka)

#tanbahkan nilai 333 pada index ke-1
#print panjang listnya
#print isi listnya

#NO_8_contoh_2
my_list = [] #membuat list kosong

#mengisi list dengan append yang berulang
for i in range(5):
    my_list.append(i + 1)

print("\n", my_list)

#NO_9_contoh_2
my_list = [] #membuat list kosong

for i in range(5):
    my_list.insert(0, i + 1)

print("\n", my_list)

#NO_10
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print("\n", total)

#NO_11
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print("\n", total)

#NO_12
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print("\n", my_list)

#NO_13_kuis_20
#Langkah 1
exo = []
print("\nLangkah 1: ", exo)

#Langkah 2
exo.append("Suho, Kai, Chanyeol, Sehun")
print("Langkah 2: ", exo)

# Langkah 3
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_baru:
    exo.append(anggota)
print("Langkah 3:", exo)

# Langkah 4
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4:", exo)

# Langkah 5
exo.insert(len(exo) - 2, "Xiumin")
print("Langkah 5:", exo)

# Jumlah anggota
print("Jumlah anggota exo:", len(exo))