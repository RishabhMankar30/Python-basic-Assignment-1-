#Question 1:
def is_symmertical(num):
    if type(num)==int:
        string_num=str(num)
        if string_num=="".join(reversed(string_num)):  #we converted int into str bcz, int can not reverse by this method.
            return "True"
        else:
            return "False"

print(is_symmertical(7227))
print(is_symmertical(12567))
print(is_symmertical(44444444))
print(is_symmertical(9939))

print("----------------------------------------------------------------------------------------------------------------")

#Question 2:
def multiply_nums(s):
    l=s.split(", ") # here delimiter(seperator) we have kept is comma and space(, ), inorder to seperate only values.
    mul=1
    for i in l:
        mul=mul*int(i)
    return mul

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))
print("----------------------------------------------------------------------------------------------------------------")

#Question 3:
def square_digit(n):
    s = str(n)  # converted int into str, for iteration
    l = []
    for i in s:
        sq = int(i) ** 2
        num_str = str(sq)  # convert int into str, bcz join will work only on string.
        l.append(num_str)
    j = "".join(l)
    con_int = int(j)  # convert str into int, bcz final output should be int.
    return con_int

print(square_digit(9119))
print(square_digit(2483))
print(square_digit(3212))
print("----------------------------------------------------------------------------------------------------------------")

#Question 4:
def setify(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return(l1)

l=[1, 3, 3, 5, 5]
print(setify(l))
l1=[4, 4, 4, 4]
print(setify(l1))
l2=[5, 7, 8, 9, 10, 15]
print(setify(l2))
l3=[3, 3, 3, 2, 1]
print(setify(l3))
print("----------------------------------------------------------------------------------------------------------------")

#Question 5:

def mean(num):
    if type(num)==int:
        string=str(num)
        sum=0
        for i in string:
            sum=sum+int(i)
        mean=sum/len(string)
        return mean

print(mean(42))
print(mean(12345))
print(mean(666))

