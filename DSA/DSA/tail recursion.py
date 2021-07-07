# def tail(n):
#     # print(n)
#     return tail(n-1)
# tail(5)

def tail_factorial(x, totalSoFar = 1):
    if x == 0:
        return totalSoFar
    else:
        return tail_factorial(x-1, totalSoFar * x)
print(tail_factorial(997))

#   PYTHON does not support tail recursion optimization.
