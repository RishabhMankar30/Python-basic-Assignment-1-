#Question1.
def evenly_divisible(a, b, c):
    l1 = []
    for i in range(a, b + 1):
        if i % c == 0:
            l1.append(i)
    print("the sum of evenly divisible :", sum(l1))
    if sum(l1) == 0:  # means there is  no number in list .
        return "No number between {} and {} can be evenly divided by {}".format(a, b, c)


print(evenly_divisible(1, 10, 3))
print("------------------------------------------------------------------------------------------------------------")

#Question2.
def expression_check(s):
    check=eval(s)
    return check
"""eval() function: eval() is not much used due to security reasons:
>You may want to use it to allow users to enter their own “scriptlets”: 
small expressions can be use with this function to evaluate the expression.
>eval is also sometimes used in applications needing to evaluate math expressions
>** The data pass inside the eval() function must be in string format."""

print(expression_check("3<7<11"))
print(expression_check("13>44>33>1"))
print(expression_check("1<2<6<9>3"))

print("------------------------------------------------------------------------------------------------------------")

#Question3.
def replace_vowels(string,char):
    vowels="AEIOUaeiou"
    count=0
    for i in vowels:
        if i in string:
            string=string.replace(i,char)
            count=count+1
    if count==0:
        print("No vowels are there in this string")
    return string


s="the aardvark&quot"
print(replace_vowels(s,"#"))

print("------------------------------------------------------------------------------------------------------------")
#Question4.
 ##method 1:
def factorial(num):
    if type(num)==int:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return "Factorial of {} is --->{}".format(num, fact)


print(factorial(10))

#method2:
import math
def get_factorial(num):
    f=math.factorial(num)
    return "Factorial of {} is --->{}".format(num,f)
print("------------------------------------------------------------------------------------------------------------")

#Question 5
"""You are given two strings of equal length, you have to find the Hamming Distance between these string.
Where the Hamming distance between two strings of equal length is the number of "same positions" at two string
at which the corresponding character is different."""
def Humming(s1,s2):
    l=[]
    for i in range(len(s1)): #or range(len(s2)) bcz both have equal length.
        if s1[i]!=s2[i]:
            l.append(i)
    c=len(l)
    return "The humming distance {},{} is--->{}".format(s1,s2,c)


s1="strong"
s2="strung"
print(Humming(s1,s2))