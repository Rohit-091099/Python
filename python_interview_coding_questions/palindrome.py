# Write a Python program to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

main_string = input("Enter a string: ")
input_string = main_string.lower()
input_string = input_string.replace(" ", "")
if is_palindrome(input_string):
    print(f"{main_string} is a palindrome.")
else:
    print(f"{main_string} is not a palindrome.")


# Condsider the following rulles:
# Case-insensitive check → "Madam" should count as palindrome.
# Ignore spaces/punctuation → "A man a plan a canal Panama".
# Number palindromes → "1221" or 12321.