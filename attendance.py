import sys
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")