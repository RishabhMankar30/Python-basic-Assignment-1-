#Question 1:
import math
try:
    N = input("Enter a numbers:")
    print("the numbers are:")
    for D in N.split(","):
        print(D, end=",")
    print("\n")
    print("The Output:")
    for D in N.split(","):
        C = 50
        H = 30
        Q = round(math.sqrt((2 * C * int(D) / H)))
        print(Q,end=",")
    print("\n")
except Exception as e:
    print(e)

print("------------------------------------------------------------------------------------------------")



#Question 2:

r = int(input("Input number of rows: "))
c= int(input("Input number of columns: "))
array = [[ 0 for col in range(c)] for row in range(r)]

for row in range(r):
    for col in range(c):
        array[row][col]= row*col

print(array)

print("------------------------------------------------------------------------------------------------")

#Question 3:

try:
    unsorted=input("Enter a list of the words").split(",")  # by default split convert words into list.
    print("The list of unsorted words=",unsorted)
    unsorted.sort()
    print("list of words after sorting=",unsorted)
except Exception as e:
    print(e)

print("------------------------------------------------------------------------------------------------")

#Question 4:

try:
    s = input("Enter a list of the words:").split(" ")  #by default split convert words into list.
    list_unique = []
    for i in s:
        if i not in list_unique:
            list_unique.append(i)
    list_unique.sort()
    print("The list of word after removing duplicate and sorting is=", list_unique)

    print("The word seperated by whitespace after removing duplicate and sorting:")
    for j in list_unique:
        print(j, end=" ")
except Exception as e:
    print(e)

print("------------------------------------------------------------------------------------------------")

#Question 5:
try:
    s = input("enter a string: ")
    letters = 0
    digits = 0
    for i in s:
        if i.isalpha():
            letters = letters + 1
        elif i.isdigit():
            digits = digits + 1
    print("DIGITS={}, LETTERS={}".format(digits, letters))
except Exception as e:
    print(e)

print("------------------------------------------------------------------------------------------------")

#Question 6:

import re
p= input("Enter the multiple password to check correct one").split(",")
try:
    for i in p:
        x = True
        while x:
            if (len(i) < 6 or len(i) > 12):
                break
            elif not re.search("[a-z]", i):
                break
            elif not re.search("[A-z]", i):
                break
            elif not re.search("[$#@]", i):
                break
            elif re.search("\s", i):  # "\s" is use to check the blank spaces in a string.
                break
            else:
                print("This is a valid password:", i)
                break
        print("This is NOT valid password",i)
except Exception as e:
    print(e)

print("Method-2")

# Method-2
p= input("Enter the multiple password to check correct one").split(",")
u,l,s,d= 0,0,0,0
for i in p:
    if len(i) >= 6 or len(i) <= 12:
        for j in i:
            if j.isupper():
                u = u + 1
            if j.islower():
                l = l + 1
            if j == "#" or j == "@" or j == "$":
                s = s + 1
            if j.isdigit():
                d = d + 1
    if (u >= 1 and l >= 1 and s >= 1 and d >= 1 and u + l + s + d == len(i)):
        print("Password is valid:",i)
    else:
        print("Password is NOT valid:",i)

print("------------------------------------------------------------------------------------------------")








