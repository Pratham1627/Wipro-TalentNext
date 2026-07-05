# Return the sum of all numbers in a list.
def sum_list(numbers):
    return sum(numbers)

numbers = [8, 2, 3, 0, 7]

print("Sum =", sum_list(numbers))


# Return the reverse of a string.
def reverse_string(string):
    return string[::-1]

string = input("Enter a string: ")

print("Reversed String:", reverse_string(string))


# Calculate and return the factorial of a number.
def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

num = int(input("Enter a number: "))

print("Factorial =", factorial(num))


# Accept a string and print the number of uppercase
# and lowercase letters in it.
def count_case(string):

    upper = 0
    lower = 0

    for ch in string:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)

string = input("Enter a string: ")

count_case(string)


# Print the even numbers from a given list.
def even_numbers(numbers):

    even = []

    for num in numbers:

        if num % 2 == 0:
            even.append(num)

    print("Even Numbers:", even)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(numbers)


# Check whether a number is prime or not.
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime")
