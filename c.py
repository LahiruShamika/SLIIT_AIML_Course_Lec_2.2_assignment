"""
c) Create a program to input five marks of a student and display the grades. 

• Mark > 75 – A 

• Mark 65 to 75 – B 

• Mark 55 to 64 – C 

• Mark 45 to 54 – S 

• Mark < 45 – F 

"""

def get_grade(mark):
    if mark > 75:
        return 'A'
    elif 65 <= mark <= 75:
        return 'B'
    elif 55 <= mark <= 64:
        return 'C'
    elif 45 <= mark <= 54:
        return 'S'
    else:
        return 'F'

marks = []

for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Please enter a valid number.")

print("\nGrades for the entered marks:")
for i, mark in enumerate(marks, start=1):
    grade = get_grade(mark)
    print(f"Mark {i}: {mark} - Grade: {grade}")
