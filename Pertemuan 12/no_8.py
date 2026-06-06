#no 8
def cek_segitiga(a,b,c):
    return a + b > c and b + c > a and c + a > b

print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))