#no 11
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial(n-1)