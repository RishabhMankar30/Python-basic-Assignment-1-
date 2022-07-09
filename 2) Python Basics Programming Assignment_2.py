import logging
logging.basicConfig(filename="assignment_2.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
class Assignment_2:
    logging.info("we are into python programming assignment 2 class")
    #1. Write a Python program to convert kilometers to miles?
    def km_to_mile(self,km):
        try:
            logging.info("convert km into mile")
            logging.info("the km is --->%s",km)
            mile=km*0.6213
            logging.info("the quantity converted in mile is---> %s",mile)
            return mile
        except Exception as e:
            logging.exception(e)
    #2. Write a Python program to convert Celsius to Fahrenheit?
    def cel_to_far(self,celcius):
        try:
            logging.info("convert celcius to fahrenhite")
            logging.info("the celcius quantity is ---> %s",celcius)
            fahrenhite=(celcius*1.8)+32
            logging.info("the qualtity converted in Fahrenheit is--->%s",fahrenhite)
            return fahrenhite
        except Exception as e:
            logging.exception(e)
    #3. Write a Python program to display calendar?
    def calendar(self,yy,mm):
        try:
            logging.info("the calender of given year and month is being display")
            import calendar
            cal=calendar.month(yy,mm)
            logging.info("the calendar is this---> %s",cal)
            return cal
        except Exception as e:
            logging.exception(e)
    #4. Write a Python program to solve quadratic equation?
    def quadratic(self,a,b,c):
        try:
            logging.info("find  the roots of quadratic equaction")
            part1=(b**2-4*a*c)**0.5
            root1=(-b+part1)/(2*a)
            root2=(-b-part1)/(2*a)
            logging.info("the root of the given quad. eq ---> %s and %s",root1,root2)
            return root1, root2
        except Exception as e:
            logging.exception(e)
    #5. Write a Python program to swap two variables without temp variable?
    def swap(self,var1,var2):
        try:
            logging.info("Swap 2 variable witout using temporary variable")
            logging.info("Before swaping variable value is var1=%s and var2=%s",var1,var2)
            var1,var2=var2,var1
            logging.info("swap variables are var1= %s and var2=%s",var1,var2)
            return "Swap variables are var1={} and var2={}".format(var1,var2)
        except Exception as e:
            logging.exception(e)
assin_2obj=Assignment_2()
print(assin_2obj.km_to_mile(5))
print(assin_2obj.cel_to_far(1))
print(assin_2obj.calendar(2022,7))
print(assin_2obj.quadratic(10,20,30))
print(assin_2obj.swap(10,20))










