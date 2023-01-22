
# HEAD RECURSION
def fibonacci(n):
    
    # BASE CASES (2)
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    # recursive call
    num1 = fibonacci(n-1)
    num2 = fibonacci(n-2)

    # operation
    result = num1 + num2

    return result

    
print(fibonacci(6))

