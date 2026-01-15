students = {
    "Asha": "Python",
    "Ravi": "Data Antytics",
    "Neha": "AI"
}
print("Student Names:")
for name in students.keys():
    print(name)

print("\nEnrolled Courses:")
for course in students.values():
    print(course)
search_name = input("\nEnter student name to check: ")

if search_name in students:
    print(f"Yes, {search_name} exists and enrolled in {students[search_name]}")
else:
    print(f"No, {search_name} does not exist in the list.")
