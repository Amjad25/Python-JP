# Assignmnet #1 Amjad Ali Khan 23/05/2024

# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""
#code Pronlem 1
inpt = float(input("Enter a float number: "))
inpt_rounded = round(inpt, 2)
print(f"Original number: {inpt}\nRounded number: {inpt_rounded}")
print(f"Length of the number entered by user :: {len(str(inpt))}")

# problem 2
"""
Problem Statement:

Prompt the user to enter a sentence.
Convert the entire sentence to uppercase.
Convert the entire sentence to lowercase.
Capitalize the first word of the sentence.

Print each of these modified sentences.
"""

# input_sentence = input("Enter a sentence: ")
# print(f"Uppercase: {input_sentence.upper()}")
# print(f"Lowercase: {input_sentence.lower()}")
# print(f"Capitalized: {input_sentence.split(" ")[0].capitalize()}")

# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""

# input_sentence = input("Enter a sentence: ")
# input_word = input("Enter the word to replace: ")
# input_replace = input("Enter the word to replace with: ")
# print(f"Original sentence: {input_sentence}")
# print(f"Modified sentence: {input_sentence.replace(input_word, input_replace)}")


# problem 4

"""
Write a program that:
Asks the user to enter their age.
Adds 10 to their age.

Prints a message saying "In 10 years, you will be X years old." where X is the new age.
"""
# input_age = int(input("Enter your age: "))
# new_age = input_age + 10
# print(f"In 10 years, you will be {new_age} years old.")

# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

# input_name = input("Enter your full name: ")
# input_number = int(input("Enter your favorite number: "))
# print(f"Your name in uppercase: {input_name.upper()}")
# new_number = input_number * 2
# print(f"Your favorite number multiplied by 2 is {new_number}.")

# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""
# input_first_name = input("Enter your first name: ")
# input_last_name = input("Enter your last name: ")
# full_name = input_first_name + " " + input_last_name
# full_name_upper = full_name.upper()
# modified_sentence = full_name.replace(" ", "-")
# full_name_length = len(full_name)
# print("Your full name in uppercase is: " + full_name_upper)
# print("Modified sentence: " + modified_sentence)
# print("The length of your full name is: " + str(full_name_length))

# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""

# input_num1 = float(input("Enter the first number: "))
# input_num2 = float(input("Enter the second number: "))
# average = (input_num1 + input_num2) / 2
# print(f"The average of the two numbers is {round(average, 2)}")\

# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""

input_sentence = input("Enter a sentence: ")
modified_sentence = input_sentence.replace(" ", "_")
words = input_sentence.split(" ")
print(f"Modified sentence: {modified_sentence}")
print(f"Words: {words}")


