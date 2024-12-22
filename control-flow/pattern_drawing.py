# pattern_drawing.py
# A script to draw a square pattern of asterisks using while and for loops.

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Avoid newline, print asterisks side by side
    print()  # Print a newline after each row
    row += 1  # Move to the next row
