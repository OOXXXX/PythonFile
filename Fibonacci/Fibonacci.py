def fib(n):
    assert n >= 0
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(fib(i), end=" ")
