import logging
logging.basicConfig(filename="assign-4.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
class assign_4:
    logging.info("We are inside the assign_4 class")
    #1. Write a Python Program to Find the Factorial of a Number?
    def factorial(self):
        try:
            logging.info("we are taking input to find factorial.")
            num=int(input("Enter a no. to get the factorial---->"))
            logging.info("The number is---->%s",num)
            fact=1
            for i in range(1,num+1):
                fact= fact*i
            logging.info("The Factorial of the number is---->%s",fact)
            return fact
        except Exception as e:
            logging.exception(e)
    #2. Write a Python Program to Display the multiplication Table?
    def multi_table(self):
        try:
            logging.info("The multiplication table of a given number is")
            num=int(input("Enter the number of which you need multiplication"))
            logging.info("we have to find out the %s multiplication table",num)
            for j in range(1,11):
                 multi = num * j
                 print(num,"*",j,"=",multi)
            logging.info("Above is the multiplication table of the %s",num)
        except Exception as e:
            logging.exception(e)
    #3. Write a Python Program to Print the Fibonacci sequence?
    def fibo(self):
        try:
           logging.info("Find the fibonaci series")
           num=int(input("Enter how many numbers you want in series"))
           logging.info("We need %s  numbers in a series",num)
           a=0
           b=1
           l=[]
           for i in range(num):
                l.append(a)
                a, b = b, a + b
           logging.info("The fibinaci series is---->%s",l)
           return l
        except Exception as e:
            logging.exception(e)
    #4. Write a Python Program to Check Armstrong Number?
    def armstrong(self):
        try:
            logging.info("we are checking for an armstrong number")
            num=str(input("Enter a number to check armstrong number"))
            logging.info("The number is %s",num)
            sum=0
            for i in range(len(num)):
                sum=sum+(int(num[i])**len(num))
            if sum==int(num):
                logging.info("The %s is a armstrong",int(num))
                return int(num),"<----Thenumber is Armstrong number",
            else:
                logging.info("The %s number is not a armstrong number")
                return int(num),"<----The is not a Armstrong number",
        except Exception as e:
            logging.exception(e)
    #5. Write a Python Program to Find Armstrong Number in an Interval?
    def arms_inter(self):
        try:
            logging.info("We are finding the armstrong number in between interval")
            start=int(input("Enter the starting point"))
            logging.info("The starting point of the number is---->%s",start)
            end=int(input("Enter the ending point"))
            logging.info("The ending point of the number is---->%s", end)
            l=[]
            for i in range(start,end+1):
                str_digit=str(i)
                sum=0
                for j in range(len(str_digit)):
                    sum=sum+(int(str_digit[j])**len(str_digit))
                if sum==i:
                    logging.info(" %s<----is armstrong number",i)
                    l.append(i)
            return "The list of armstrong number is---->",l
        except Exception as e:
            logging.exception(e)
    #6. Write a Python Program to Find the Sum of Natural Numbers?
    def sum_nat(self):
        try:
            logging.info("We are finding sum of natural numbers")
            end=int(input("Enter the ending number, upto which you want sum of natural number---->"))
            logging.info("The ending number, upto which we need sum of natural number is ---->%s",end)
            sum=0
            for i in range(1,end+1):
                sum=sum+i
            logging.info("The sum of all natural number is---->%s",sum)
            return sum
        except Exception as e:
            logging.exception(e)
assin4_obj=assign_4()
print(assin4_obj.factorial())
print(assin4_obj.fibo())
print(assin4_obj.multi_table())
print(assin4_obj.armstrong())
print(assin4_obj.arms_inter())
print(assin4_obj.sum_nat())

























