"""
d)  Write a program to input a series of numbers
terminated by -999. Calculate and print the sum
of the numbers entered. 

"""

total_sum = 0

print("Enter numbers one by one (Enter -999 to stop):")

while True:
    try:
        number = float(input("Enter a number: "))
        if number == -999:
            break
        total_sum += number
    except ValueError:
        print("Please enter a valid number.")

print(f"\nThe sum of the numbers entered is: {total_sum}")
