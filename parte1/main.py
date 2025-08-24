from fibonacci import *
sys.setrecursionlimit(2000)
def run():
    for i in range(100):
        print(fibonacci_rec(100))


def run2():
    for i in range(100):
        print(fibonacci_rec(i))

run2()