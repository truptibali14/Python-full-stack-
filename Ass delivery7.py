distance = float(input("Enter delivery distance in km: "))
if distance <= 5:
    print("Category: Local")
elif distance <= 20:
    print("Category: City")
else:
    print("Category: Outstation")
