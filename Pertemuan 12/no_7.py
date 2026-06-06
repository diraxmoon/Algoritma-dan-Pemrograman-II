#no 7
def cek_segitiga(a,b,c):
    if a + b <= c or b + c <=a or c + a <=b:
        return False
    return True

print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))