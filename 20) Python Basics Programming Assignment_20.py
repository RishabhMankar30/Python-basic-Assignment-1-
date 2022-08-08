#Question1:
def filter_list(l):
    int_lst=[]
    if type(l)==list:
        for i in l:
            if type(i)==int:
                int_lst.append(i)
        return int_lst

l1=[1,2,3,"a","b",4]
l2=["A",0,"Edabit","1729",1729,"python"]
l3=["nothing","here"]
print(filter_list(l1))
print(filter_list(l2))
print(filter_list(l3))
print("---------------------------------------------------------------------------------------------------------------")

#Question2:
def add_indexes(l):
    l1=[]
    if type(l)==list:
        for i in range(len(l)):
            a=i+l[i]
            l1.append(a)
        return l1


l1=[0,0,0,0,0]
l2=[1,2,3,4,5]
l3=[5,4,3,2,1]
print(add_indexes(l1))
print(add_indexes(l2))
print(add_indexes(l3))
print("---------------------------------------------------------------------------------------------------------------")
#Question3:

def cone_volume(height,radius):
    import math
    vol= ((3.1415/3)*(radius**2)*height)
    return "The cone volume radius: {}, height: {}= {}".format(radius,height,round(vol,2))

print(cone_volume(3,2))
print(cone_volume(15,6))
print(cone_volume(18,0))
print("---------------------------------------------------------------------------------------------------------------")
#Question4:
def triangle_dot(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return "The no. of dots in {}th triangle= {}".format(n,sum)

print(triangle_dot(215))
print(triangle_dot(6))
print(triangle_dot(1))
print("---------------------------------------------------------------------------------------------------------------")
#Question 5:
#Create a function that takes a list of ""numbers between 1 and 10"" (excluding one number) and
#returns the missing number.
def Missing_num(l):
    if type(l)==list:
        for i in range(1,10+1):
            if i not in l:
                return "Missing No.={}".format(i)


l=[1,2,4,5,6,7,8,9]
l1=[7,6,5,9,3,4,1,2,8]
l3=[10,5,1,2,4,6,8,3,9]
print(Missing_num(l))
print(Missing_num(l1))
print(Missing_num(l3))

