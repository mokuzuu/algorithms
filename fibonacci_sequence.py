import functools


@functools.lru_cache()
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


f = {}


def fib2(n):
    if n <= 1:
        return 1
    else:
        if n in f:
            return f[n]

        a = fib2(n - 1) + fib2(n - 2)
        f[n] = a
        return a


def fib3(n):
    if n == 0:
        return 1
    else:
        f1, f2, f3 = 1, 1, 1
        for i in range(n - 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f2


# print(fib(5))
# print(fib2(998))
print(fib3(3))
