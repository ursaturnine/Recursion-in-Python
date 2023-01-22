
# variable and accumulator
def factorial(n, result=1):

    if n == 1:
        return result
    
    return factorial(n-1, n * result)
    
    
factorial(4)