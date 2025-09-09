# Write a Python program to find the largest element in a list.

def largest_element(list):
    number = list[0]
    for i in list:
        if i > number:
            number = i
    return number

list = input("Enter a list of numbers: ")
list = list.split()
list = [int(i) for i in list]
print(f"The largest element in the list is {largest_element(list)}")