def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

print("Simple Interest is:", simple_interest(p, r, t))
