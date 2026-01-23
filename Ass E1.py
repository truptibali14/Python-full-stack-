def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

print("Prime numbers between", a, "and", b, "are:")
print_primes(a, b)
