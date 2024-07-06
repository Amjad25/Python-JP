# FILE METHODs

# 1. open()
# 2. read()
# 3. write()
# 4. close()
# 5. readlines()
# 6. writelines()
# 7. append()
# 8. seek()
# 9. tell()
# 10. readline()
# 11. truncate()

# try:
#     file = open("book_1.txt", "r")
#     data =file.read()
#     print(data)
# except Exception as e:
#     print("Got Error: ", e)


# Create a file “commentary.txt” using open function and add content
# “Over 1: The match begins with a cracking cover drive for four by the opener! The crowd is already buzzing.”

# file = open("commentary.txt", "w")
# file.write("Over 1: The match begins with a cracking cover drive for four by the opener! The crowd is already buzzing.")

# # Read file “commentary.txt” and display its content
# file = open("commentary.txt", "r")
# data = file.read()
# print(data)

# # Update file “commentary.txt” and add more content
# # “Over 3: A brilliant outswinger from the bowler! The batsman edges it, but it falls just short of the slip fielder.”
# file = open("commentary.txt", "a")
# file.write("\nOver 3: A brilliant outswinger from the bowler! The batsman edges it, but it falls just short of the slip fielder.")

# # Read file “commentary.txt” and using len function see if it has 2 items
# file = open("commentary.txt", "r")
# data = file.readlines()
# print(len(data))


# file.writable()


# json pickel
# import json
# # json.dumps() - convert python object to json string
# # json.loads() - convert json string to python object
# # json.dump() - write python object to json file
# # json.load() - read json file and convert it to python object

for i in range(1, 6):
    print("##"*i)

# diamond pattern
for i in range(1, 6):
    print(" "*(5-i)+"**"*i)
for i in range(4, 0, -1):
    print(" "*(5-i)+"**"*i)

# diamond pattern for *
for i in range(1, 6):
    print(" "*(5-i)+"* "*i)
for i in range(4, 0, -1):
    print(" "*(5-i)+"* "*i)


# mutable defination
# mutable means changeable & memory location is not changed
# list, dict, set are mutable
# list1 = [1, 2, 3, 4]
# list1[0] = 5

# immutable defination
# immutable means not changeable & memory location is changed
# tuple, string, int, float are immutable
# tuple1 = (1, 2, 3, 4)
# tuple1[0] = 5




