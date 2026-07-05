# Accept two numbers from the user and perform division.
# If any exception occurs, print an error message.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except Exception as e:
    print("Error:", e)


# Accept a number from the user and check whether it is prime.
# If the user enters anything other than a number, handle the exception.
try:
    num = int(input("Enter a number: "))

    if num < 2:
        print("Not Prime")
    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime")
        else:
            print("Not Prime")

except ValueError:
    print("Invalid Input. Please enter a number.")


# Accept the file name from the user.
# If the file exists, print its contents in title case.
# Otherwise, handle the exception.
try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    content = file.read()

    print(content.title())

    file.close()

except FileNotFoundError:
    print("File does not exist.")


# Declare a list with 10 integers and ask the user to enter an index.
# Check whether the number at that index is positive or negative.
# Handle invalid index exceptions.
numbers = [10, -5, 25, -30, 45, -60, 70, -80, 90, -100]

try:
    index = int(input("Enter an index (0-9): "))

    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Invalid Index.")

except ValueError:
    print("Please enter a valid integer.")
