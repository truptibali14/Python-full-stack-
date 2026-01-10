employee_name=input("enter employee name:")
salary=float(input("enter salary:"))
rating=int(input("enter performance rating (1-5):"))
if rating == 5:
   bonus_percentage = 0.20
elif rating == 4:
   bonus_percentage = 0.15
elif rating == 3:
   bonus_percentage = 0.10
else:
   bonus_percentage = 0.0
bonus_amount = salary*bonus_percentage
final_salary = salary+bonus_amount
print("employee name :",employee_name)
print("performance rating :",rating)
print("bonus amount :",bonus_amount)
print("final salary :",final_salary)
