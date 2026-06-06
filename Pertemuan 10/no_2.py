#Array 2 dimensi
KOSONG = "."
Benteng = "B"
Kuda = "K"

papan_catur = []
for i in range(8):
    baris = [KOSONG for i in range(8)]
    papan_catur.append(baris)

papan_catur[0][0] = Benteng
papan_catur[0][7] = Benteng
papan_catur[7][0] = Benteng
papan_catur[7][7] = Benteng

papan_catur[4][2] = Kuda

# Tampilkan papan catur
print("  0 1 2 3 4 5 6 7")
for i in range(8):
    print(i, end=" ")
    for j in range(8):
        print(papan_catur[i][j], end=" ")
    print()