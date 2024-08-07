# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content
"""
file = open("user_email.txt", "w")
for i in range(3):
    user = input("Enter user name: ")
    title = input("Enter title: ")
    link = input("Enter link: ")
    file.write(f"\n\nHi {user}!\n\nWe've found the best article for you based on your interest: {title}\nPlease click {link} to open the article")

file.close()
"""

# Create a new text file named "student_records.txt" with the following initial content:
# Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# Open "updated_records.txt" in append mode('a') and add a new student record:
# Close the "updated_records.txt" file.

# Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.


"""file = open("student_records.txt", "w")
file.write("Student ID | Student Name | Grade\n101       | Alice        | A\n102       | Bob          | B\n103       | Carol        | C")
file.close()

file = open("student_records.txt", "r")
data = file.readlines()
print(data)
file.close()

file = open("updated_records.txt", "w")
file.write("Student ID | Student Name | Grade")
for line in data:
    if "A" in line or "B" in line:
        file.write(line)
file.close()"""


"""
### Assignment: Password Manager Program
Demo: https://www.youtube.com/watch?v=O8596GPSJV4

#### Objective:
Create a password manager program that allows users to store, retrieve, and manage their passwords. 
The program will use file handling to save and read data, and it will be run in the terminal.

#### Requirements:
1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
3. **Basic Operations**:
    - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
    - **Retrieve a password**: Ask for the website and return the username and password.
    - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

#### Program Flow:
1. Display a menu with the following options:
    - Add a new password
    - Retrieve a password
    - Delete a password
    - Exit
2. Based on the user's choice, perform the corresponding operation.
3. Repeat the menu until the user chooses to exit.

#### Detailed Instructions:
1. **Menu Display**: Create a function to display the menu and get the user's choice.
2. **Add Password**:
    - Prompt the user for the website, username, and password.
    - Write this information to a file in a structured format.
3. **Retrieve Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Display the username and password.
4. **Delete Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Remove the entry and update the file.
5. **File Format**: Store each entry in a new line in the format:
    ```
    website,username,password
    ```

#### Example:
1. **Add Password**:
    ```
    Enter website: example.com
    Enter username: user1
    Enter password: pass123
    Password saved successfully!
    ```
2. **Retrieve Password**:
    ```
    Enter website: example.com
    Username: user1
    Password: pass123
    ```
3. **Delete Password**:
    ```
    Enter website: example.com
    Password deleted successfully!
    ```

#### Hints:
- Use functions to keep your code organized.
- Use lists and dictionaries to manage the data in memory before writing to or reading from the file.
- Ensure to handle cases where the file may not exist initially.
"""


fileName = "password_manager.txt"
file = open(fileName, "w")
file.write("website,username,password")
file.close()

def display_menu():
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    file = open(fileName, "a")
    file.write(f"\n{website},{username},{password}")
    file.close()
    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    file = open(fileName, "r")
    data = file.readlines()
    for line in data:
        if website in line:
            website, username, password = line.split(",")
            print(f"Username: {username}")
            print(f"Password: {password}")
            break
    else:
        print("Website not found!")
    file.close()

def delete_password():
    website = input("Enter website: ")
    file = open(fileName, "r")
    data = file.readlines()
    file.close()

    if website not in str(data):
        print("Website not found!")
        return
    file = open(fileName, "w")

    for line in data:
        if website not in line:
            file.write(line)
    file.close()
    print("Password deleted successfully!")

while False:
    
    choice = display_menu()
    if choice == 1:
        add_password()
    elif choice == 2:
        retrieve_password()
    elif choice == 3:
        delete_password()
    elif choice == 4:
        break
    else:
        print("Invalid choice! Please try again.")


"""
create the same program again but this time file data should be stored in json
"""

import json

fileName = "password_manager.json"
file = open(fileName, "w")
file.write("[]")
file.close()

def display_menu():
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    file = open(fileName, "r")
    data = json.load(file)
    file.close()
    data.append({"website": website, "username": username, "password": password})
    file = open(fileName, "w")
    json.dump(data, file)
    file.close()
    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    file = open(fileName, "r")
    data = json.load(file)
    file.close()
    for entry in data:
        if entry["website"] == website:
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
            break
    else:
        print("Website not found!")

def delete_password():
    website = input("Enter website: ")
    file = open(fileName, "r")
    data = json.load(file)
    file.close()
    for entry in data:
        if entry["website"] == website:
            data.remove(entry)
            file = open(fileName, "w")
            json.dump(data, file)
            file.close()
            print("Password deleted successfully!")
            break
    else:
        print("Website not found!")

while False:
        
        choice = display_menu()
        if choice == 1:
            add_password()
        elif choice == 2:
            retrieve_password()
        elif choice == 3:
            delete_password()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")




"""
create the same program again but this time file data should be stored in binary using pickle module

"""

import pickle

fileName = "password_manager.pkl"
file = open(fileName, "wb")
data = []
pickle.dump(data, file)
file.close()

def display_menu():
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    file = open(fileName, "rb")
    data = pickle.load(file)
    file.close()
    data.append({"website": website, "username": username, "password": password})
    file = open(fileName, "wb")
    pickle.dump(data, file)
    file.close()
    print("Password saved successfully!")


def retrieve_password():
    website = input("Enter website: ")
    file = open(fileName, "rb")
    data = pickle.load(file)
    file.close()
    for entry in data:
        if entry["website"] == website:
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
            break
    else:
        print("Website not found!")

def delete_password():
    website = input("Enter website: ")
    file = open(fileName, "rb")
    data = pickle.load(file)
    file.close()
    for entry in data:
        if entry["website"] == website:
            data.remove(entry)
            file = open(fileName, "wb")
            pickle.dump(data, file)
            file.close()
            print("Password deleted successfully!")
            break
    else:
        print("Website not found!")

while True:

    choice = display_menu()
    if choice == 1:
        add_password()
    elif choice == 2:
        retrieve_password()
    elif choice == 3:
        delete_password()
    elif choice == 4:
        break
    else:
        print("Invalid choice! Please try again.")  

