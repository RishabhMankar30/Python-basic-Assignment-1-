#Question1:
def equal(a,b,c):
    l=[a,b,c]
    for i in l:
        c = l.count(i)
        if c > 1:
            return c
        else:
            return 0

print(equal(3,4,3))
print(equal(1,1,1))
print(equal(3,4,1))
print("--------------------------------------------------------------------------------------------------------")
#Question2:
def dict_to_list(d):
    t=d.items()
    l=[]
    for i in t:
        l.append(i)
    l.sort()
    return l

d1={"D":1,"B":2,"C":3}
print(dict_to_list(d1))
d2={"likes":2,"dislikes":3,"followers":10}
print(dict_to_list(d2))
print("--------------------------------------------------------------------------------------------------------")

#Question3:

def mapping(l):
    d={}
    for i in l:
        d[i]= i.upper() # to find element is dict d[key], if we have to add element is dictionary then--> d["key"]="value", this will automaticaly append key-value pair in dict.
    return d

l1=["p", "s"]
print(mapping(l1))
l2=["a","b","c"]
print(mapping(l2))
l3=["a", "v", "y", "z"]
print(mapping(l3))
print("--------------------------------------------------------------------------------------------------------")

#Question4:
def vow_replace(string,vow):
    vowels=["a","A","e","E","i","I","o","O","u","U"]
    for i in vowels:
        if i in string:
            string = string.replace(i, vow)
    return string

s="apples and bananas"
print(vow_replace(s,"u"))
s1="cheese casserole"
print(vow_replace(s1,"o"))
s2="stuffed jalapeno poppers"
print(vow_replace(s2,"e"))
print("--------------------------------------------------------------------------------------------------------")

#Question5:
def ascii_capitalize(string):
    l=[]
    for i in string:
        if ord(i)%2==0:
            l.append(i.upper())
        else:
            l.append(i.lower())
    str_updated="".join(l)
    return str_updated

s4="to be or not to be!"
print(ascii_capitalize(s4))
s5="THE LITTLE MERMAID"
print(ascii_capitalize(s5))
s6="Oh what a beautiful morning."
print(ascii_capitalize(s6))









