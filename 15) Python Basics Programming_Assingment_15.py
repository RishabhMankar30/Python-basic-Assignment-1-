#Question 1:
def div_5_7(n):
    l=[]
    for i in range(n+1):
        if i%5==0 and i%7==0:
            l.append(i)
    yield l

for j in div_5_7(100):
    print(j)
print("--------------------------------------------------------------------------------------------------")

#Question 2:
def even(n):
    le=[]
    for i in range(n+1):
        if i%2==0:
            le.append(i)
    yield le

for j in even(10):
    print(j)
print("--------------------------------------------------------------------------------------------------")

#Question 3:

n=int(input("Enter a number"))
s = [0, 1]
s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(n)]
print (s)
print("--------------------------------------------------------------------------------------------------")

#Question 4:

s=input("Enter the email_is in the format username@companyname.com: ")
l=s.split("@")
username=l[0]
print("The mail username=",username)
print("--------------------------------------------------------------------------------------------------")

#Question 5:

class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return "The area is=",(self.length*self.length)

s=square(2)
print(s.area())
print("--------------------------------------------------------------------------------------------------")














