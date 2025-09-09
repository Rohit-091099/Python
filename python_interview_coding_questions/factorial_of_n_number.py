# Write a Python program to find the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")