#Question1:
def next_in_line(l,i):
    try:
        if l==[]:
            return "No list has been selected"
        if type(l)==list and type(i)==int:
            l.append(i)
            l.remove(l[0])
            return l

    except Exception as e:
        print(e)

l=[5, 6, 7, 8, 9]
l1=[7, 6, 3, 23, 17]
l3=[]
print(next_in_line(l,6))
print(next_in_line(l1,10))
print(next_in_line(l3,6))

print("---------------------------------------------------------------------------------------------------------------")

#Question2:

def get_budget(l):
    try:
        sum=0
        if type(l)==list:
            for d in l:
                sum=sum+d["budget"]
            return "sum of budget= {}".format(sum)
    except Exception as e:
        return e

l=[
 { "name": "John", "age": 21, "budget": 23000 },
 { "name": "Steve", "age": 32, "budget": 40000 },
 { "name": "Martin", "age": 16, "budget": 2700 }
]
print(get_budget(l))

l2=[
 { "name": "John", "age": 21, "budget": 29000 },
 { "name": "Steve", "age": 32, "budget": 32000 },
 { "name": "Martin", "age": 16, "budget": 1600 }
]
print(get_budget(l2))
print("---------------------------------------------------------------------------------------------------------------")
#Question3:

#method1:
def alphabet_sort(s):
    try:
        l=[]
        for i in s:
            l.append(i)
        for i in l:
            print(i,end="")
        print("\n")
        return "This is the the alphabetically sorted string"
    except Exception as e:
        return e

s="hello"
print(alphabet_sort(s))

#method2:
# using sorted() function
def sort_alphabetically(s):
    l=sorted(s)
    sort_string="".join(l)
    print(sort_string)

s1="geek"
print(sort_alphabetically(s1))
print("---------------------------------------------------------------------------------------------------------------")

#Question4:
import math
def compound_interest(p,t,r,n):
    ci=p*((1+(r/n))**(n*t))
    return round(ci,2)

print(compound_interest(100,1,0.05,1))
print(compound_interest(10000, 10, 0.06, 12))
print(compound_interest(3500, 15, 0.1, 4))
print("---------------------------------------------------------------------------------------------------------------")

#Question5:

def return_only_integer(l):
    int_lst=[]
    if type(l)==list:
        for i in l:
            if type(i)==int:
                int_lst.append(i)
        return int_lst

l1=[9, 2, "space", "car", "lion", 16]
l2=["hello", 81, "basketball", 123, "fox"]
l3=[10, "121", 56, 20, "car", 3, "lion"]
l4=["String", True, 3.3, 1]
print(return_only_integer(l1))
print(return_only_integer(l2))
print(return_only_integer(l3))
print(return_only_integer(l4))
