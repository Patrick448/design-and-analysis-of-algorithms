from functools import lru_cache
import sys
sys.setrecursionlimit(10000000)

def fibonacci_iter(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        f1 = 1
        f2 = 1

        for i in range(2,n):
            f = f1 + f2
            f1 = f2
            f2 = f

        return f

@lru_cache(maxsize=None)
def fibonacci_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)



#AI implementations
def ai_fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def ai_fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return ai_fibonacci_recursive(n - 1) + ai_fibonacci_recursive(n - 2)
