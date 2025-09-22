def fib(n):
    if n == 1 or n == 0 :
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = 12
for i in range(n):
    print(fib(i), end = ' > ')