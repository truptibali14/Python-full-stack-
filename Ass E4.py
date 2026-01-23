def fibonacci(n):
    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

num = int(input("Enter how many Fibonacci numbers: "))
print("Fibonacci series:", fibonacci(num))
