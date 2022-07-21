import logging
logging.basicConfig(filename="assi_5.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
logging.info("we are solving python programming assignment_5")
class assign_5:
    logging.info("we are writting the assignment5")
    def hcf_find(self,n1,n2):
        logging.info("we are finding the HCF of two number")
        #2. Write a Python Program to Find HCF?
        try:
           logging.info("the first number is--> %s and the second number is-->%s",n1,n2)
           small=min(n1,n2)
           logging.info("The smallest number out of two number is-->small")
           for i in range(small,0,-1):
               logging.info("we are into for loop interating over number from small to 1")
               logging.info("trying to divide the both the number by interating numbers")
               if n1 % i == 0 and n2 % i == 0:
                   logging.info("our condition get fulfill and got the hcf. which can divide both the number ")
                   hcf = i
                   logging.info("the HCF is--->%s", i)
                   return "The HCF of {},{} is{}".format(n1, n2, hcf)
        except Exception as e:
            logging.exception(e)

    """Notes for HCF: -->The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers 
    is the largest positive integer that perfectly divides the two given numbers.
    -->CONCEPT: for HCF, we first determine the smaller of the two numbers since the H.C.F can only be less than or equal to the smallest number.
    --->In the function, we first determine the smaller of the two numbers since the H.C.F can only be less than or equal to the smallest number."""

    def LCM_find(self,n1,n2):
        #1. Write a Python Program to Find LCM?
        logging.info("we are finding the LCM of 2 number ")
        try:
            logging.info("First we are finding a hcf")
            def first_hcf(n1,n2):
                small = min(n1, n2)
                for i in range(small + 1, 0, -1):
                    if n1 % i == 0 and n2 % i == 0:
                        hcf = i
                        return hcf
        except Exception as e:
            logging.exception(e)
        try:
            logging.info("now we are finding lcm")
            logging.info("the first number is--> %s and the second number is-->%s", n1, n2)
            logging.info("we are applying the formula and used hfc_find() function as well")
            lcm = (n1 * n2) //first_hcf(n1,n2)   # we are calling function inside another function inside same class.
            logging.info("the lcm of two no. is--->%s", lcm)
            return "the LCM of numbers {},{} is:{}".format(n1, n2, lcm)
        except Exception as e:
            logging.exception(e)
    def conversion(self):
        #3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
        logging.info("Here we are solving decimal to binary and octal to hexadecimal")
        try:
            #part 1: decimal to binary
            logging.info("Decimal to Binary conversion")
            deci=int(input("enter a decimal number"))
            logging.info("The decimal no. is--->%s",deci)
            l=[]
            while deci!=0:
                logging.info("we are into thr loop, till quotient=0")
                remainder=deci%2
                deci=deci//2
                l.append(remainder)
            logging.info("The decimal no.--> %s converted into binary is--> %s",deci,l[::-1])
            return "the decimal no.{}, converted into binary is {}".format(deci,l[::-1])
        except Exception as e:
            logging.exception(e)
        #we can also use inbuilt function for decimal to binary i.e. bin(dec)
        #we can also use inbuilt function for decimal to binary i.e.oct(dec)
        #we can also use inbuilt function for decimal to hexadecimal i.e. hex(dec)
        try:
            #part2: octal to hexadecimal
            logging.info("Convert octal to hexadecimal")
            octal = input("Enter a octal digit")
            logging.info("The octal digit is %s",octal)
            decimal=int(oct(octal,8)) #this octal no. will be in string format for this in built function
            logging.info("octal no. is converted into decimal-->%s",deciaml)
            hexa=hex(decimal)
            logging.info("the hexadecimal no. is--->%s",hexa)
        except Exception as e:
            logging.exception(e)
    def give_chr_num(self):
        try:
           logging.info("finding the ascii value of character")
           #4. Write a Python Program To Find ASCII value of a character?
           character=input("Enter the character whose ascii value to be found: ")
           logging.info("the given character is---> %s",character)
           value=ord(character) #ord("str word") gives ascii value of chartecter, chr(int) gives the character of value define in ascii table
           logging.info("the ascii value of the character--> %s, ascii value--->%s",character,value)
           return "the ascii value of the character--> {}, ascii value--->{}".format(character,value)
        except Exception as e:
            logging.exception(e)
a=assign_5()
print(a.hcf_find(24,18))
print(a.LCM_find(12,18))
print(a.conversion())
print(a.give_chr_num())


class calculator:
    logging.info("We are into class: calculator, where we are solving 4 basic operation")
    def add(self):
        try:
            logging.info("We are performing addition operation")
            num1 = float(input("enter a 1st number to perform addition: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("enter a 2nd number to perform addition: "))
            logging.info("2nd no. is-->%s", num2)
            addition = num1 + num2
            logging.info("The addition of two no. is=%s", addition)
            print("{} + {} = {}".format(num1, num2, addition) )
        except Exception as e:
            logging.exception(e)

    def subtract(self):
        try:
            logging.info("We are performing subtraction operation")
            num1 = float(input("enter a 1st number to perform subtraction: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("enter a 2nd number to perform subtraction: "))
            logging.info("2nd no. is-->%s", num2)
            Subtraction = num1 - num2
            logging.info("The Suntraction of two no. is = %s", Subtraction)
            print("{}  -  {} = {}".format(num1, num2, Subtraction))
        except Exception as e:
            logging.exception(e)

    def multi(self):
        try:
            logging.info("We are performing multiplication operation")
            num1 = float(input("enter a 1st number to perform Multiplication: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("Enter a 2nd number to perform Multiplication: "))
            logging.info("2nd no. is-->%s", num2)
            Multiplication = num1 * num2
            logging.info("The Subtraction of two no. is = %s", Multiplication)
            print("{} * {} = {}".format(num1, num2, Multiplication))
        except Exception as e:
            logging.exception(e)

    def divid(self):
        try:
            logging.info("We are performing division operation")
            num1 = float(input("Enter a 1st number to perform division: "))
            logging.info("The 1st number is--> %s", num1)
            num2 = float(input("Enter a 2nd number to perform division: "))
            logging.info("The 2nd number is--> %s", num2)
            Division = num1 / num2
            logging.info("The Division of two no. is = %s", ans)
            print("{} / {} = {}".format(num1, num2, Division))
        except Exception as e:
            logging.exception(e)
c=calculator()
print("1.Addition\n","2.Subtraction\n","3.Multiplication\n","4.Division\n")

while(True):
    select = int(input("Select the number to perform operation: "))
    if select == 1:
        c.add()
        conti = input("Do you want to continue for next operation yes! or no!: ")
        if conti=="yes!":
            pass
        else:
            break
    elif select == 2:
        c.subtract()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break
    elif select == 3:
        c.multi()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break
    elif select == 4:
        c.divid()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break
    else:
        print("Oh! error occor. You have selected a wrong number.")


























