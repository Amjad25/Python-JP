# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).

temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]
week_2 = temperatures[7:14]
print(week_2)


# Task 2
"""
Extracting a Substring from a Sentence
Objective: Given a sentence, extract and print a specific word using string slicing.
sentence = "The quick brown fox jumps over the lazy dog"
extract third word "brow"
"""

sentence = "The quick brown fox jumps over the lazy dog"
third_word = sentence[10:14]
print(third_word)


"""
Extracting a Sublist of Favorite Colors
Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
extract first three colors
"""

favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
first_three_colors = favorite_colors[:3]
print(first_three_colors)


# Write a Python program to check if a list is empty or not.
list1 = []
if not list1:
    print("List is empty")
else:
    print("List is not empty")


# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc
for i in range(1, 11):
    print(i)
        
# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc
for i in range(35, 51):
    print(i)

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc
for i in range(-15, -26, -1):
    print(i)

# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc
for i in range(5, -11, -1):
    print(i)

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc
for i in range(0, 51, 3):
    print(i)

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")


# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

list1 = [3, 5, 2, 1, 4]
x = 0
for i in list1:
    x += i
print(x)

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

list1 = [3, 5, 2, 1, 4]
x = 0
for i in list1:
    if i > x:
        x = i
print(x)


# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50]
sum1 = 0
for i in numbers:
    sum1 += i
print(sum1)


# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

numbers = [12, 7, 9, 24, 18, 5, 3, 20]
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in range(len(fruits)):
    print(f"Index: {i} Element: {fruits[i]}")

# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

even_numbers = []
for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)


# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

even_numbers = []
for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)



