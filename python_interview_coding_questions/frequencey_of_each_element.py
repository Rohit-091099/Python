# Write a Python program to count the frequency of each element in a list.

def frequency_of_each_element(list):
    frequency = {}
    for i in list:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

list = input("Enter a list of numbers: ")
list = list.split()
list = [int(i) for i in list]
print(f"The frequency of each element in the list is {frequency_of_each_element(list)}")