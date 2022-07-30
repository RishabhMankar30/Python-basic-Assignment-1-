#Question 1:
class generator:
    def div_by_7(self, n):
        for i in range(0, n):
            if i % 7 == 0:
                yield i

g=generator()
for j in g.div_by_7(100):
    print(j)

print("-----------------------------------------------------------------------------------------------------")

#Question 2:
s=input("Enter a string you want:")
l=s.split(" ")  # converting string element into list using space as a seperator
non_repeate=[]  # storing all the non repetative element in list.
for i in l:
    if i not in non_repeate:
        non_repeate.append(i)
non_repeate.sort()  # sorting the non repetative element list.
print(non_repeate)
for j in non_repeate:  # counting the element occurance in list through non repatative element list.
    c= l.count(j)
    print(j,":",c)

print("-----------------------------------------------------------------------------------------------------")

#Question 3:

class person:
    def getGender(self,m):
        return m
class Male(person):
    pass
class Female(person):
    pass
p= person()
print(p.getGender("unknown"))
m=Male()
print(m.getGender("Male"))
f=Female()
print(f.getGender("Female"))


print("-----------------------------------------------------------------------------------------------------")

#Question 4:

sub=["I","you"]
verb=["Play","Love"]
obj=["Hockey","Football"]
#Note: to form any setence there is formula subject+verb+object

for s in sub:
    for v in verb:
        for o in obj:
            print(s+v+o)  # or print(s,v,o) we can use

print("-----------------------------------------------------------------------------------------------------")

#Question 5:

import gzip
s = b"hello world!hello world!hello world!hello world!."  # this b infront of string convert the string into bytes form.
s = gzip.compress(s)   # note variable s with string and compress is same.
print("compressed string=",s)

de = gzip.decompress(s)
print("decompressed string=",de)
print("-----------------------------------------------------------------------------------------------------")

#Question 6:
def bi_search(lst,ele):
    lb=0
    ub=len(lst)-1
    while ub>=lb:
        mid=(ub+lb)//2
        if lst[mid]==ele:
            return "The element {} is at index {}".format(ele,mid)
        elif ele>lst[mid]:
            lb=mid+1
        else:
            ub=mid-1
    return "element did not found"

lst = [1, 3, 5, 7,10]
print(bi_search(lst, 5))

print("-----------------------------------------------------------------------------------------------------")