"""
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
Write a Python program to create a calculator class. Include methods for basic arithmetic operations
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.



In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses

"""

class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
    def enroll(self, course):
        if course in Student.available_courses:
            self.courses.append(course)
        else:
            print(f"{course} is not available")
        
    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course)
            
    def list_available_courses(self):
        print("Available Courses:")
        for course in Student.available_courses:
            print(course)

student1 = Student("Ali", 20)
student2 = Student("Ahmed", 22)
student3 = Student("Sara", 21)

student1.enroll("English")
student1.enroll("Urdu")
student1.enroll("Physics")
student1.enroll("Math")
student1.enroll("Chemistry")
student1.enroll("Islamyat")

student2.enroll("English")
student2.enroll("Urdu")
student2.enroll("Physics")
student2.enroll("Math")
student2.enroll("Chemistry")

student3.enroll("English")
student3.enroll("Urdu")
student3.enroll("Physics")
student3.enroll("Math")
student3.enroll("Chemistry")

print("Student 1 courses List \n ")
student1.list_courses()

print("Student 1 available courses List \n ")

student1.list_available_courses()

print("Student 2 courses List \n ")
student2.list_courses()
print("Student 2 available courses List \n ")

student2.list_available_courses()
print("Student 3 courses List \n ")

student3.list_courses()
print("Student 3 available courses List \n ")
student3.list_available_courses()

