print("available course:")
print("1.python programming->5000")
print("2.data analytics->8000")
print("3.AI & ML->12000")
course_choice=int(input("enter course number(1/2/3):"))
if course_choice==1:
    course_name="python programming"
    fee = 5000
elif course_choice==2:
    course_name="data analytics"
    fee = 8000
elif course_choice==3:
    course_name="AI & ML"
    fee = 12000
else:
  print("Invalid course selection!")
  exit()
student = input("Are you a student(yes/no):").lower()
early = input("Early registration(yes/no):").lower()
discount = 0
if student=="yes":
    discount+=0.10*fee
if early=="yes":
    discount+=0.05*fee
final_amount=fee-discount
print("course name:",course_name)
print("Original Fee:",fee)
print("Total discount:",discount)
print("Final payable amount:",final_amount)

    
    
