import logging
logging.basicConfig(filename="assign_3.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
class assign_3:
    logging.info("We are into the assign_3 class")
    def no_check(self,value):
        try:
            logging.info("Here we are checking no. is +ve,-ve,or zero")
            logging.info("checking for a positive number")
            if value>0:
                logging.info("it is a positive number--->%s",value)
                return "the Given value is Positive",value
            elif value<0:
                logging.info("checking for a negative number--->%s",value)
                return "the Given value is  negative",value
            else:
                logging.info("the given no is zero--->%s",value)
                return "the Given value  is  Zero",value
        except Exception as e:
            logging.exception(e)
    #2. Write a Python Program to Check if a Number is Odd or Even?
    def odd_even(self,value):
        try:
            logging.info("Here we are checking the number is Even or Odd")
            if value%2==0:
                logging.info("the given no is even--->%s", value)
                return "Given no. is Even--->", value

            else:
                logging.info("the given no. is odd--->%s", value)
                return "Given no. is odd--->", value
        except Exception as e:
            logging.exception(e)
    #3. Write a Python Program to Check Leap Year.
    def leap_year(self,year):
        try:
            logging.info("We are verifying the year is leap or not")
            if year%4==0 or year%400==0:
                logging.info("the year is a leap year--->%s",year)
                return "the year is a leap  year",year
            else:
                logging.info("the year is not leap year--->%s",year)
                return year, "the year is not a leap year"
        except Exception as e:
            logging.exception(e)
    #4. Write a Python Program to Check Prime Number?
    def prime(self,num):
        try:
            logging.info("Checking for Prime number")
            for i in range(2, num):
                if num % i == 0:
                    logging.info("%s<---This is not a prime no", num)
                    print(num, "<---The no. is not a prime no.")
                    break
            else:
                 print("The number is a prime no.:-",num)
        except Exceptiona as e:
            logging.exception(e)
    #5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
    def prime_1_10000(self):
        try:
            logging.info("checking for prime number between 1 to 10,000")
            num = int(input("Enter the  no. between 1 to 10000 to check prime or not ="))
            logging.info("the given number is--->%s",num)
            for i in range(2, num):
                if num%i==0:
                    logging.info("%s<---This number is not a prime number")
                    print(num,"<---the entered number is not a prime number")
                    break
            else:
                logging.info("%s<---this is a prime number")
                print(num,"<---The number is a prime number")
        except Exception as e:
            logging.exception(e)
obj_3=assign_3()

print(obj_3.odd_even(88))
print(obj_3.no_check(-6))
print(obj_3.leap_year(2022))
print(obj_3.prime(6))
print(obj_3.prime_1_10000())

































