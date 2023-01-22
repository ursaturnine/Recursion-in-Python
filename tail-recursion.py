def tail(n):

    # BASE CASE
    if n == 0:
        return

    # first we do some operations
    print(n)

    # recursive call
    tail(n-1)
tail(5)
"""Output
5
4
3
2
1

# tail recursion is similar to a for loop
for n in range(5, 0 , 1):
    print(n)
"""