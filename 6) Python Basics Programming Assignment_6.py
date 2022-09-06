#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
print("----------------------------------------------------------------------------------------------------------------")
#2. Write a Python Program to Find Factorial of Number Using Recursion?

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)

num=5
if num<0:
    print("factorial does not exist")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("factorial of {} is {}".format(num,fact(num)))
print("----------------------------------------------------------------------------------------------------------------")
#3. Write a Python Program to calculate your Body Mass Index?
weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in meter: "))
BMI= weight/(height**2)
print("Your BMI is= {} kg/m2".format(round(BMI)))
print("----------------------------------------------------------------------------------------------------------------")

#4. Write a Python Program to calculate the natural logarithm of any number?
num=float(input("Enter a number whose natural log is to be find out"))
import math
natural_log=math.log(num)
print("The natural log of {} is {}".format(num,round(natural_log)))
print("----------------------------------------------------------------------------------------------------------------")

#5. Write a Python Program for cube sum of first n natural numbers?
n_range=int(input("Enter a how many natural number cube sum do you need: "))
cube_sum=0
for i in range(1,n_range+1):
    cube_sum=cube_sum+(i*i*i)

print("The cube_sum of all the {} natural nubers is={}".format(n_range,cube_sum))
print("----------------------------------------------------------------------------------------------------------------")







