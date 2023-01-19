import sys

#Recursive Method
def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

#Dynamic Programming Method
def fibonacci(n):
    f = [0 for x in range(n+1)]
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(sys.stdin.readline())
print(fib(n), fibonacci(n))
