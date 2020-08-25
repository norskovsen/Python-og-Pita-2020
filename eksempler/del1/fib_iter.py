def fib_iter(x):
    fib_n, fib_n_1 = 0, 1
    for i in range(x):
        fib_n, fib_n_1 = fib_n_1, fib_n+fib_n_1
    return fib_n

while True:
    print(fib_iter(int(input("fib> "))))
