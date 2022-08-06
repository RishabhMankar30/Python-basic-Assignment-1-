#Question1:
def double_char(s):
    if type(s)==str:
        for i in s:
            print(i+i, end="")
    print("\n")
    return "these is the string with  repeated words "

print(double_char("String"))

print(double_char("1234!_ "))
print("--------------------------------------------------------------------------------------------------------------")

#Question2:
def reverse(b):
    if type(b)==bool:
        if b==True:
            return False
        elif b==False:
            return True
    else:
        return "boolean expected"

print(reverse(0))

print(reverse(True))
print("--------------------------------------------------------------------------------------------------------------")

#Question3:
def num_layers(n):
    thickness=0.5
    folded_thickness= thickness*(2**n)  #paper thichness get 2 power thickness everytime we fold.
    return "The paper thickness after folding {} times= {} meters".format(n,folded_thickness/1000) #converted into meter

print(num_layers(21))
print("--------------------------------------------------------------------------------------------------------------")

#Question4:
def index_of_caps(string):
    lst=[]
    for i in string:
        if i.isupper():
            index = string.index(i)
            lst.append(index)
    lst.sort()    #this will sort the list by default in accending order
    return lst

print(index_of_caps("eQuINoX"))
print("--------------------------------------------------------------------------------------------------------------")
#Question5:
def even(n):
    """This function gives the list of even number in between range 1 to n"""
    ev = [i for i in range(1,n+1) if i % 2 == 0]
    return ev

print(even(8))
print(even(2))

print("--------------------------------------------------------------------------------------------------------------")
