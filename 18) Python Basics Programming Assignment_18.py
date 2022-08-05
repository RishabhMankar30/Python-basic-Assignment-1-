#Question 1:
def filter_list(l):
    f_list=[]
    for i in l:
        if type(i)== int and i>=0:
            f_list.append(i)
    return "the list of integer num={}".format(f_list)

l=[1,2,"rish","a",55,0,1,2,"ass","a","123",123]
print(filter_list(l))
print("----------------------------------------------------------------------------------------------------------------")

#Question 2:
def reversed(string):
    rev=string[::-1]
    case=rev.swapcase()
    return "the after reversing with opposite case= {}".format(case)
s="ReVeRsE"
print(reversed(s))
print("----------------------------------------------------------------------------------------------------------------")
#Question 3:

first,*middle,last=[1,2,3,4,5,6]
print(first)
print(middle)
print(last)
"""**This is Destructuring a list(Unpacking a list)
>  first take-> very first element of list
> last take-> very last element of list
>middle take-> all middle element in between list
** it is similar like
-first=l[0]
-last=l[-1] or l[len(l)-1]
-Middle=l[1:5]
---->head, *tail = [1, 2, 3, 4, 5]
head give= 1
tail gives=[2,3,4,5]
**similar as
head=l[0]
tail=[1::]"""
print("----------------------------------------------------------------------------------------------------------------")
#Question 4:
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return "factorial({})= {}".format(num,f)

print(fact(5))
print(fact(1))

#method2:
import math
def facto(num):
    factorial=math.factorial(num)
    return "Factorial of num {} = {}".format(num,factorial)
print("----------------------------------------------------------------------------------------------------------------")

#Question 5:

def move_to_end(l,n):                         # l: list n: element to be  remove.
    l1=[]
    while True:
        if n in l:                          # searching element in a list l.(No matters how many times it is present in list)
            l.remove(n)                    # if element found, we are removing it from origional list.
            l1.append(n)                  # after getting element, we are storing that element in another empty list l1.
        else:
            break                        # if required element not present in list break the loop.
    l.extend(l1)                         # Now we have Two list, l which was origional one but removed the require element from it and
                                         # l1 is the list which have required element
    return "the list after appending the required element:{}".format(l)    # here we have "append" all the required elements from list l1 to l, using extend function

lst=[1,3,2,4,4,1]
print(move_to_end(lst,1))

li=["a","a","a","b"]
print(move_to_end(li,"a"))

print("----------------------------------------------------------------------------------------------------------------")