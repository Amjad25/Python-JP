# Write a program to check whether a person is eligible to vote or not?

input_age = int(input("Enter your age: "))
if input_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Write a program to check char is vowel or not.

input_char = input("Enter a character: ")
if input_char in ['a', 'e', 'i', 'o', 'u']:
    print("Character is vowel")
else:
    print("Character is not vowel")


# Write a program to check if number is positive or negative

input_number = int(input("Enter a number: "))
if input_number < 0:
    print("Number is negative")
else:
    print("Number is positive")

# Write a program to check whether a number is odd or even?

input_number = int(input("Enter a number: "))
if input_number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100


subject_math_score = int(input("Enter your marks out of 100: "))
if subject_math_score >= 90:
    print("Grade A")
elif subject_math_score >= 80:
    print("Grade B")
elif subject_math_score >= 70:
    print("Grade C")
else:
    print("Grade D")
# Write a program to check if a number is divisible by 7 or not

input_number = int(input("Enter a number: "))
if input_number % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

# Write a program to check if year is leap year.

input_year = int(input("Enter a year: "))
if input_year % 4 == 0:
    print("Year is leap year")
else:
    print("Year is not leap year")

# Write a program to ask user its name and check whether name consists of 5 or more letters

input_name = input("Enter your name: ")
if len(input_name) >= 5:
    print("Name consists of 5 or more letters")
else:
    print("Name consists of less than 5 letters")

# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = input("Enter operator: ")
if input3 == '+':
    print(input1 + input2)
elif input3 == '-':
    print(input1 - input2)
elif input3 == '*':
    print(input1 * input2)
elif input3 == '/':
    print(input1 / input2)
else:
    print("Invalid operator")


# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"

input1 = int(input("Enter a number: "))
if input1 % 2 == 0 and input1 % 3 == 0:
    print(f"{input1} is divisible by 2 and 3")
elif input1 % 2 == 0:
    print(f"{input1} is only divisible by 2")
elif input1 % 3 == 0:
    print(f"{input1} is only divisible by 3")
else:
    print(f"{input1} is not divisible by 2 and 3")


# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
if input1 > input2:
    print(f"{input1} is larger than {input2}")
else:
    print(f"{input2} is larger than {input1}")
    
# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))
if input1 > input2 and input1 > input3:
    print(f"{input1} is largest")
elif input2 > input1 and input2 > input3:
    print(f"{input2} is largest")
else:
    print(f"{input3} is largest")


# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop

input_color = input("Enter color: ")
if input_color.lower() == 'green':
    print("Car is allowed to go")
elif input_color.lower() == 'red':
    print("Car has to stop")
elif input_color.lower() == 'yellow':
    print("Car has to wait")
else:
    print("Invalid color")


"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""

salary = int(input("Enter salary: "))
years_of_service = int(input("Enter years of service: "))
if years_of_service < 5:
    print("No bonus")
elif years_of_service >= 5 and years_of_service <= 10:
    print(f"Bonus is {salary * 0.10}")
else:
    print(f"Bonus is {salary * 0.20}")


"""
create the same ATM machine program that we do in last class.

Features:
Affiliated Card Requirement:
Allow transactions only if the user has an affiliated card (affiliated_card is True) and the user's age is less than 60 years (age < 60).

Senior Citizen Exception:
Allow transactions for senior citizens (is_senior_citizen is True) regardless of their affiliated card status.

Government Employee Exception:
Allow transactions for government employees (is_govt_employee is True) regardless of their age and affiliated card status.

Additional Charge for Low Grade:
Charge an additional 10 Rs for transactions if the user's grade (grade) is less than 18.

# hint: filename: if_statement/if_with_nested_if.py
"""

affiliated_card = True
age = 59
is_senior_citizen = False
is_govt_employee = False
grade = 17
if (affiliated_card and age < 60) or is_senior_citizen or is_govt_employee:
    if grade < 18:
        print("Charge an additional 10 Rs")
    print("Allow transactions")
else:
    print("Do not allow transactions")

    



