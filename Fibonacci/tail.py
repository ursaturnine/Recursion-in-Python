

def fibonacci(n, a=0, b= 1):
    if n == 1:
        return b
    if n == 0: 
        return a

    return fibonacci(n-1, b, a+ b)
print(fibonacci(6))