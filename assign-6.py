"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76





4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}

# 1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

for student, score in student_scores.items():
    print(f"Student: {student}, Score: {score}")

# 2. Write a for loop to calculate the average score of the students. Print the average score.
total_score = 0
for score in student_scores.values():
    total_score += score

average_score = total_score / len(student_scores)

# 3. Write a for loop to assign grades based on the following criteria:
# Score >= 90: Grade A
# Score >= 80 and < 90: Grade B
# Score >= 70 and < 80: Grade C
# Score < 70: Grade D
# Store these grades in a new dictionary called student_grades.
student_grades = {}
for student, score in student_scores.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    student_grades[student] = grade

print(student_grades)

# 4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. Print the updated student_scores dictionary.

for student in student_scores:
    student_scores[student] += 5
print(student_scores)


"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

"""
employee_data = {
    "John": 55000,
    "Emma": 60000,
    "Harry": 70000,
    "Sophia": 65000,
    "Mike": 48000
}

# 1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.

for employee, salary in employee_data.items():
    if salary > 60000:
        print(employee)

#2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.

for employee in employee_data:
    employee_data[employee] *= 1.1
print(employee_data)

"""
Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2
"""
library_books={
  "The Great Gatsby": 4,
  "1984": 6,
  "To Kill a Mockingbird": 3,
  "The Catcher in the Rye": 5,
  "Moby Dick": 2
}

# 1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.
for book, copies in library_books.items():
  library_books[book] = copies + 2

print(library_books)

total_books = 0

#2. Write a for loop to calculate the total number of books in the library. Print the total count.
for copies in library_books.values():
  total_books += copies

print(f"Total number of books: {total_books}")


"""
============================================================================================
consider the list of dicts
book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
Write a for loop to assign one more detail "stock" based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e book_list.
"""
book_list = [
    {"name": "The Great Gatsby", "quantity": 4},
    {"name": "1984", "quantity": 6},
    {"name": "To Kill a Mockingbird", "quantity": 3},
    {"name": "Moby Dick", "quantity": 2},
]

for book in book_list:
  copies = book["quantity"]
  if copies >= 5:
    book["stock"] = "Popular"
  elif copies >= 3:
    book["stock"] = "Available"
  else:
    book["stock"] = "Limited"

print(book_list)

"""
============================================================================================================
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

"""

students = {
  "Alice": {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [85, 90, 78],
    "Class": 10
  },
  "Bob": {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [75, 80, 88],
    "Class": 10
  },
  "Charlie": {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [92, 89, 94],
    "Class": 11
  },
  "Diana": {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [88, 76, 85],
    "Class": 11
  },
  "John": {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [50, 60, 60],
    "Class": 11
  }
}

# 1. Display Alice English Score
print(f"Alice's English score: {students['Alice']['Scores'][2]}")

# 2. Display Bob Class
print(f"Bob's Class: {students['Bob']['Class']}")

# 3. Display Charlie Math Score
print(f"Charlie's Math score: {students['Charlie']['Scores'][0]}")

# 4. Display Diana's avg score
avg_score = sum(students['Diana']['Scores']) / len(students['Diana']['Scores'])
print(f"Diana's average score: {avg_score:.2f}")  # Format to 2 decimal places

# 5. Display John's all subject name and score
print(f"Student: John, Scores:")
for i, subject in enumerate(students['John']['Subjects']):
  score = students['John']['Scores'][i]
  print(f"\tSubject: {subject}, Score: {score}")

# 6. Add new Student (Example: Emma)
new_student = "Emma"
students[new_student] = {
  "Subjects": ["History", "Art", "Music"],
  "Scores": [80, 95, 70],
  "Class": 12
}

# 7. Add new subject and score to John (Example: Social Studies, 75)
students['John']['Subjects'].append("Social Studies")
students['John']['Scores'].append(75)

print("\nUpdated student dictionary:")
print(students)

"""
Givent the list of students
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. display which class obtained the higher marks
7. display the student name that obtain high marks in subject Math in class 10
8. Add new Student and its subject, score and class in same dict i.e students
"""
students = [
  {
    "name": "Alice",
    "subjects": ["Math", "Science", "English"],
    "scores": [85, 90, 78],
    "Class": 10
  },
  {
    "name": "Bob",
    "subjects": ["Math", "Science", "English"],
    "scores": [75, 80, 88],
    "Class": 10
  },
  {
    "name": "Charlie",
    "subjects": ["Math", "Science", "English"],
    "scores": [92, 89, 94],
    "Class": 11
  },
  {
    "name": "Diana",
    "subjects": ["Math", "Science", "English"],
    "scores": [88, 76, 85],
    "Class": 11
  }
]

# 1. Display Alice English Score
alice = students[0]  # Access Alice's data (first element)
print(f"Alice's English score: {alice['scores'][2]}")

# 2. Display Bob Class
bob = students[1]  # Access Bob's data (second element)
print(f"Bob's Class: {bob['Class']}")

# 3. Display Charlie Math Score
charlie = students[2]  # Access Charlie's data (third element)
print(f"Charlie's Math score: {charlie['scores'][0]}")

# 4. Display Diana's avg score
diana = students[3]  # Access Diana's data (fourth element)
avg_score = sum(diana['scores']) / len(diana['scores'])
print(f"Diana's average score: {avg_score:.2f}")

# 5. Display John's all subject name and score (assuming John doesn't exist)
# Comment out if you want to handle John (see note below)
john_not_found = True
for student in students:
  if student["name"] == "John":
    john_not_found = False
    john = student
    print(f"Student: {john['name']}, Scores:")
    for i, subject in enumerate(john['subjects']):
      score = john['scores'][i]
      print(f"\tSubject: {subject}, Score: {score}")
    break
if john_not_found:
  print("John not found in the student list.")

# 6. Display class with highest marks
highest_class_score = 0
highest_class = None
for student in students:
  class_score = sum(student['scores'])
  if class_score > highest_class_score:
    highest_class_score = class_score
    highest_class = student['Class']

print(f"Class with highest marks: {highest_class}")

# 7. Display student with highest Math score in class 10
highest_math_score = 0
highest_math_student = None
for student in students:
  if student['Class'] == 10 and student['scores'][0] > highest_math_score:
    highest_math_score = student['scores'][0]
    highest_math_student = student['name']

print(f"Student with highest Math score in class 10: {highest_math_student}") if highest_math_student else print("No student in class 10.")

# 8. Add new Student (Example: Emma)
new_student = {
  "name": "Emma",
  "subjects": ["History", "Art", "Music"],
  "scores": [80, 95, 70],
  "Class": 12
}
students.append(new_student)

print("\nUpdated student list:")
print(students)


