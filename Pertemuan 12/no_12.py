#no 12
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)