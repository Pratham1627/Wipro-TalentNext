# Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Check if a number is Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Check whether two numbers have the same last digit
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)


# Print numbers from 1 to 10 in a single row
for i in range(1, 11):
    print(i, end="\t")


# Print even numbers between 23 and 57
for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# Check if a number is Prime
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


# Print prime numbers between 10 and 99
for num in range(10, 100):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)


# Sum of digits of a number
num = int(input("Enter a number: "))

digit_sum = 0

while num > 0:
    digit = num % 10
    digit_sum = digit_sum + digit
    num = num // 10

print("Sum =", digit_sum)


# Reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)


# Check whether a number is Palindrome
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome.")
else:
    print(original, "is not a palindrome.")
