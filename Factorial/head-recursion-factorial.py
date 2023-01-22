def factorial(n):

    # base case
    if n == 0:
        return 1
    
    # use recursion -stores function calls on stack
    result1 = factorial(n-1)

    # do some operations -backtracks with return values until no more stack
    result2 = n * result1

    return result2
factorial(10)


# also return n * factorial(n-1)