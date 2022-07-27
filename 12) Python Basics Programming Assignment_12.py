#1. Write a Python program to Extract Unique values from dictionary values?
dy = {'ineuron' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'rish' : [1, 2, 5]}
l=[]
for i in dy.values():
    for j in i:
        l.append(j)
print("the list of all values= ",l)
print("The unique values in the dictionary values are=",set(l))
print("----------------------------------------------------------")

#2. Write a Python program to find the sum of all items in a dictionary?
def sum_dict(dict):
    l = []
    integer=[]
    extrac=[]
    for i in dict.items():
        for j in i:
            l.append(j)
    print("All the elements are=",l)
    for k in l:
        if type(k)==list or type(k)==int:
            integer.append(k)
    print("the integer list=",integer)
    for m in integer:
        for n in m:
            extrac.append(n)
    print("the sum of all element in dict=",sum(extrac))

sum_dict(dy)
print("----------------------------------------------------------")

#3. Write a Python program to Merging two Dictionaries?

def merg1(d1,d2):
    print("The two dictionary are 1st {} and 2nd {}".format(d1,d2))
    d3= d1.update(d2)
    print("The dictionary after merging=",d3)

d1 = {'a': 10, 'b': 8}
d2 = {'d': 6, 'c': 4}
merg1(d1,d2)
"""By using the method update() in Python, 
one dictionary can be merged into another. But in this, the second dictionary is merged into the first dictionary and no new dictionary is created. 
It returns None."""
def merg2(d1,d2):
    print("The two dictionary are 1st {} and 2nd {}".format(d1, d2))
    d3 = d1|d2
    print("The dictionary after merging=", d3)

merg2(d1,d2)
print("----------------------------------------------------------")

#4. Write a Python program to convert key-values list to flat dictionary?

from itertools import product

di={"roll_no.":[1,2,3,4,5],"student_name":["rish","amit","abhi","palash","kartik"]}
print("the given dictionary is=",di)
f= dict(zip(di["student_name"],di["roll_no."]))

print("the flat dictionary is=",f)
print("----------------------------------------------------------")

#5. Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict
d= OrderedDict([("rishabh",30),("amit",1),("nitesh",11)])
d.update({"gaju":2})
d.move_to_end("gaju",last=False)
print("The ordered dictionary=",dict(d))
print("----------------------------------------------------------")

#6. Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict
def check_order(s,p):
    d = OrderedDict.fromkeys(s)
    length=0
    for k, v in d.items():
        if k == p[length]:
            length= length+1

        if length == len(p):
            return "Yes! char. are in ordered"

    return "No! char. not in ordered"

print(check_order("ineuron is  the best", "is"))
print("----------------------------------------------------------")

#7. Write a Python program to sort Python Dictionaries by Key or Value?
from collections import OrderedDict

dictionary= {"rishabh":30,"amit":1,"nitesh":11,"naitik":22,"gaju":2}
d1=OrderedDict(sorted(dictionary.items()))
print("the dictionary sorted by keys=",dict(d1))













