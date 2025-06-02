#!/usr/bin/env python3

# Prompt the user to input the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to iterate through rows
while row < size:
    # Inner loop using for to print '*' in each column of the current row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
