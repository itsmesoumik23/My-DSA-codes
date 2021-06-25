from timeit import timeit

def fibo_recursion(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibo_recursion(n-1)+fibo_recursion(n-2)
a = timeit()
print(fibo_recursion(40))
b = timeit()
print(f"Time required in recursion: {a-b}")

def fibo_memorization(n, table={0: 1, 1: 1}):

    if n in table:
        return table[n]
    table[n] = fibo_memorization(n-1)+fibo_memorization(n-2)
    return table[n]

a = timeit()
print(fibo_memorization(40))
b = timeit()
print(f"Time required in dp: {a-b}")