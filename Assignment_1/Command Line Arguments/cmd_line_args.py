# Accept two numbers as command line arguments and display their sum.
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum =", num1 + num2)

# Accept a welcome message through command line arguments
# and display the file name along with the welcome message.
import sys

print("File Name:", sys.argv[0])
print("Welcome Message:", sys.argv[1])

# Accept 10 numbers through command line arguments
# and calculate the sum of prime numbers among them.
import sys

sum_prime = 0

for i in range(1, 11):

    num = int(sys.argv[i])

    if num < 2:
        continue

    prime = True

    for j in range(2, num):
        if num % j == 0:
            prime = False
            break

    if prime:
        sum_prime += num

print("Sum of Prime Numbers =", sum_prime)
