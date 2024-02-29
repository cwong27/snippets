def fib(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            c = a+b
            a=b
            b=c
        return b

for i in range(1, 10):
    print(fib(i))
