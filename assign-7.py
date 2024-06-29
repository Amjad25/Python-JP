# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

list1 =[100,200,300,400]
for i in enumerate(list1):
    print(i[0], i[1])


# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']
dict = {}
for i in l1:
    if i in l2:
        dict[i]=l1.count(i)+l2.count(i)
    else:
        dict[i]=l1.count(i)
for i in l2:
    if i in l1:
        dict[i]=l1.count(i)+l2.count(i)
    else:
        dict[i]=l2.count(i)
print(dict)


# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

x = 2783
counter = 0
while x>0:
    counter+=1
    x//=10
print(counter)

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

inpt = 1
while inpt!=0:
    inpt = int(input('Enter a number: '))
    if inpt!=0:
        print(inpt)
    else:
        print('you entered 0')
        break

    
# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

list1 = []
counter = 0
while counter<5:
    inpt = int(input('Enter a number: '))
    list1.append(inpt)
    counter+=1
# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

name = ''
while name!='END':
    name = input('Enter a name: ')
    print(name)
print('I am done')

# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

l1 = [11, 33, 50]
for i in l1:
    print(i, end='')



# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn


l1 = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
for i in l1:
    if len(i)>5:
        print(i)


# functions

# Write a program to create a function that takes two arguments, name and age. print them inside function.

def print_name_age(name, age):
    print(name, age)
print_name_age('Amjad', 23)

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary


def show_employee(name, salary=9000):
    print(name, salary)
show_employee('Amjad')
show_employee('Amjad', 60000)

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

def return_list(a,b,c,d):
    return [a,b,c,d]
a = 4
b = 8
c = 10
d = 12

print(return_list(a,b,c,d))

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

def km_to_miles(km):
    return km*0.621371
print(km_to_miles(10))

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

def is_divisable_by_11(num):
    if num%11==0:
        return True
    else:
        return False
print(is_divisable_by_11(22))
print(is_divisable_by_11(31))

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

def get_highest(a,b):
    if a>b:
        return a
    else:
        return b
    
print(get_highest(10,20))


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.


def fuel_cost(distance, fuel_per_liter=280):
    return distance*fuel_per_liter
print(fuel_cost(10))
print(fuel_cost(10, 300))

# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false

def is_valid_email(email):
    if len(email)>256:
        return False
    if email[0].isalnum()==False:
        return False
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    if email[email.index('@')+1:email.index('.')]=='':
        return False
    if email[email.index('.')+1:]=='':
        return False
    return True
print(is_valid_email('amjad@com'))
print(is_valid_email('amjad.com'))
print(is_valid_email('amjad@com.'))







