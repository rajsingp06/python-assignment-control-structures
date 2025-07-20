
# Task 1: Check if a number is even or odd

try:
    num = int(input("Enter an integer: "))

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

except ValueError:
    print("Please enter a valid integer.")
