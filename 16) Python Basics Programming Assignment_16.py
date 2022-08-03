#Question1.
def shutter():
    w=input("Enter a word: ")
    return w[0:2] + "... " + w[0:2] + "... " + w + "?"

print(shutter())

print("------------------------------------------------------------------------------------------------")

#Question2.
import math
def rad_deg(num):
    d = num * 57.2958
    return round(d, 1)  #this 1 representing we are rounding up to 1 decimal.

print(rad_deg(20))
print("------------------------------------------------------------------------------------------------")

#Question3.
def curzon(num):
    a=(2**num)+1
    b=(2*num)+1
    if a%b==0:
        return "is_curzon({})-->TRUE".format(num)
    else:
        return "is_curzon({})-->FALSE".format(num)

print(curzon(14))
print("------------------------------------------------------------------------------------------------")
#Question4.
import math
def area_hexagon(length):
    area= ((3*1.732)*(length**2))/2

    return "The area of Hexagon({})---> {}".format(length,round(area,1))

print(area_hexagon(3))
print("------------------------------------------------------------------------------------------------")

#Question5.
#method 1:
def deci_bin(num):
    v=bin(num).replace("0b","")
    return "Binary({})--->{}".format(num,v)

print(deci_bin(13))
print("------------------------------------------------------------------------------------------------")

#method 2:
def deci_bin1(num):
    l=[]
    while num!=0:
        r=num%2
        l.append(r)
        num=num//2
    reverse=l[::-1]
    print("Binary of given number")
    for i in reverse:
        print(i,end="")
    return "  "

print(deci_bin1(13))

