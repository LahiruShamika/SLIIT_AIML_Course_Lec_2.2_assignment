"""
b) Create a python program to input marks of 10 students
and print the maximum mark, minimum mark and
average mark of the students.

"""

marks = []

for i in range(10):
    while True:
        try:
            mark = float(input(f"Enter the mark of student {i+1}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Please enter a valid number.")

max_mark = max(marks)
min_mark = min(marks)
average_mark = sum(marks) / len(marks)

print(f"\nMaximum mark: {max_mark}")
print(f"Minimum mark: {min_mark}")
print(f"Average mark: {average_mark:.2f}")
