# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
extracted = number[0:5]
reversed_extracted = extracted[::-1]
a = input(f"Original list: {number} ")
b = input(f"Extracted first five elements: {extracted} ")
c = input(f"Reversed extracted element: {reversed_extracted} ")
print(a)
print(b)
print(c)
