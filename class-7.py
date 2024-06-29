# class 7 22/06/2024
# last class for python basics

dict ={
    "danish":200,
    "fahad":400,
    "amjad":669,
    "saad":200,
    "waleed":200,
}
# print(dict)
# dict.update({"amjad":500})
# print(dict)

# arr =[100,200,300,400,500]
# for i in arr:
#     print(arr.index(i) , i)


students=['alice','bob','charlie']
score =[80,90,100]

dict ={}
dict2 ={
    'students':[],
    'scores' :[]
}
# dict2['students'] = students
# dict2['scores'] = score

# for i , val in enumerate(students):
#     dict2['students'].append(students[i])
#     dict2['scores'].append(score[i])


# print(dict2)
# for i in enumerate(students):
#     dict[i[1]]=score[i[0]]

# print(dict)

# do while loop


x=1

x=1
# # infinite loop
# while x>0 and x<=10:
#     print(x)
    
# # will run 10 times
# while x>0 and x<=10:
#     print(x)
#     x+=1


# ask user for input postivr number and keep asking positivr numner and display
# terimante the program when user enters neagtive number

# inpt =1

# while inpt>0:
#     inpt = int(input('Enter a positive number: '))
#     if inpt>0:
#         print(inpt)
#     else:
#         print('you entered a negative number')

list1 =[10,20,30]
list2 =[40,50,60,30]

# for i in list1:
#     for j in list2:
#         if i==j:
#             print(i)
#             break
#     else:
#         continue
#     break

# # method 2
# for i in list1:
#     if i in list2:
#         print(i)


def getSumOfTwo(a,b,c):
    return a+b+c


x = getSumOfTwo(10,10,3)
print(x)


