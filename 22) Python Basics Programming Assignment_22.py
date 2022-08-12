#Question1:
def list_operation(x,y,n):
    d=[]
    for i in range(x,y+1):
        if i%n==0:
            d.append(i)
    d.sort()
    return d

print(list_operation(1,10,3))
print(list_operation(7,9,2))
print(list_operation(15,20,7))
print("-----------------------------------------------------------------------------------------------------------------")
#Question2:
def simon_says(l1,l2):  # length of both the list must be same.
    if len(l1)==len(l2):
        count=0
        for i in range(len(l1)-1):
            if l1[i]==l2[i+1]:
                count=count+1

        if count==len(l1)-1:
            return "True"
        else:
            return "False"

print(simon_says([1, 2], [5, 1]))
print(simon_says([1, 2], [5, 5]))
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
print("-----------------------------------------------------------------------------------------------------------------")

#Question3:
def society_name(l):
    if type(l)==list:
        l.sort()
        l1=[]
        for i in l:
            l1.append(i[0])
        name="".join(l1)  #we can also use print(i[0],end="") but it will give None also bcz we are not using return.
        return name

l=["Adam", "Sarah", "Malcolm"]
l1=["Harry", "Newt", "Luna", "Cho"]
l2=["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]
print(society_name(l))
print(society_name(l1))
print(society_name(l2))
print("-----------------------------------------------------------------------------------------------------------------")

#Question4:
def is_isogram(s):
    lower=s.lower()
    count=0
    for i in lower:
        c=lower.count(i)
        if c>1:
            return "False: String is not Isogram"
            break
    else:             #(***This "else" belongs to for block (it is for-else), this else will execute only when for loop completely execute with all iteration.)
        return "True:String is an Isogram"


print(is_isogram("Algorism"))

print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))
print("-----------------------------------------------------------------------------------------------------------------")

#Question5:

def is_in_order(s):
    if type(s)==str:
        l=[]
        for i in s:
            l.append(i)
        if l==sorted(l):
            return "True"
        else:
            return "False"

print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz"))



















