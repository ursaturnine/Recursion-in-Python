def head(n):

    if n == 0:
        return
    
    # recursive function call
    head(n-1)

    # do something
    print(n)
head(5)