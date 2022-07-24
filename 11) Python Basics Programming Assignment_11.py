import logging
logging.basicConfig(filename="assig_11",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
logging.info("We are solving Python Programming Basic Assignment_11")
class assig_11:
    logging.info("We are into class assig_11")

    #1. Write a Python program to find words which are greater than given length k?
    def word_length(self):
        try:
            logging.info("we are inside function,where finding words which are greater than given length k")
            s=input("Enter the string you want")
            logging.info("The given string is---> %s",s)
            num=int(input("Enter a digit,to find the length of words>than digit"))
            logging.info("The digit is %s",num)
            l=s.split(" ")  #this will split the string basis of " " space and return list of data
            l1=[]
            for i in l:
                if len(i)>num:
                    l1.append(i)
            logging.info("The list of the words, whose length> %s is --->%s",num,l1)
            print("The list of the words, whose length>{} is--> {}".format(num,l1))
        except Exception as e:
            logging.exception(e)

    #2. Write a Python program for removing i-th INDEX from a string?(***IMP***)
    def remove(self):
        try:
            logging.info("We are into function, where we are removing i-th INDEX from a string")
            s=input("Enter the string you want")
            logging.info("The Entered string is-->%s",s)
            i=int(input("Enter a INDEX, Which is to be remove from string"))
            logging.info("This--> %s INDEX will be remove from--> %s",i,s)
            a=s[:i]
            b=s[i+1:]
            string_afterremove= a+b
            logging.info("The string after removing %s Index  is---> %s",i,string_afterremove)
            return "The string after removing {} INDEX is= {}".format(i,string_afterremove)
        except Exception as e:
            logging.exception(e)
    #3. Write a Python program to split and join a string?
    def split_join(self):
        try:
            logging.info("We are into the function which will split and join the string")
            s=input("Enter the string you want")
            logging.info("The Entered string is-->%s",s)
            spl= s.split(" ")
            print("The string after spliting= {}",spl)
            logging.info("The string after spliting---> %s",spl)
            logging.info("Now we are joining that splited string")
            jo="--->".join(spl)
            print("The string after joining= {}",jo)
            logging.info("The string after joining is : %s ",jo)
        except Exception as e:
            logging.exception(e)

    #4. Write a Python to check if a given string is binary string or not?(***good logic***)
    def binary_str(self):
        try:
            logging.info("We are into the function to check it is binary or not")
            s=input("Enter the string you want")
            logging.info("The Entered string is-->%s",s)
            for i in s:
                if i=="0" or i=="1":
                    continue
                else:
                    logging.info("The Given string is NOT binary!")
                    print("The Given string {} NOT a binary!".format(s))
                break
            else:  # This for else will execute only when, for loop completed its loop fully.
                logging.info("The given string is a binary")
                print(" YES! Given string {} is a binary".format(s))
        except Exception as e:
             logging.exception(e)

    #5. Write a Python program to find uncommon words from two Strings?
    def uncommon(self):
        try:
            logging.info("We are into the function, where we are finding the uncommon words in btw tow string")
            s1=input("Enter a 1st string")
            s2=input("Enter a 2nd string")
            logging.info("The 1st string %s and  2nd string %s",s1,s2)
            l=[]
            for i in s1:
                if i not in s2:
                    l.append(i)
            else:  #here we apply condition inside a for else block.
                if l==[]:  #i.e if list is empty
                    print("there is NO uncommon words in a two string")
                    logging.info("The list is empty, means no uncommon words are found in between string")
            print("The list of uncommon words are={}".format(l))
            logging.info("The list of uncommon words is=%s",l)
        except Exception as e:
            logging.exception(e)

    #6. Write a Python to find all duplicate characters in string?
    def dulicate(self):
        try:
            logging.info("we are finding the duplicate character in a given string")
            s=input("Enter a string you want")
            logging.info("The Entered string is-->%s",s)
            l=[]
            for i in s:
                if s.count(i)>1:
                    l.append(i)
            else:
                if l==[]:
                    logging.info("There is no duplicate element in a string")
                    print("There is no duplicate element in a string")
            logging.info("The list of all duplicate element in a string is --->%s",l)
            print("The list of duplicate element is= {}",l)
        except Exception as e:
            logging.exception(e)

    #  7. Write a Python Program to check if a string contains any special character?
    def special(self):
        try:
            logging.info("we are finding the duplicate character in a given string")
            s = input("Enter a string you want")
            logging.info("The Entered string is-->%s", s)
            sp="[@_!#$%^&*()<>?/\|}{~:]" # special character set in n a string fromat.
            l=[]
            for i in s: #converting string into list(i.e seperating each and every element)
                l.append(i)
            logging.info("The list of string char= %s",l)
            print("The list of string char= {}",l)
            for j in l:  #iterating element in a list.
                if j in sp:  # checking list element in a sp.
                    print("Yes! String has a special character {}".format(j))
                    logging.info("Yes! string consist special char")
                    break
            else:
                logging.info("No! String does not have any special character")
                print("No! String does not have any special character")
        except Exception as e:
            logging.exception(e)

a=assig_11()
print(a.word_length())
print(a.remove())
print(a.split_join())
print(a.binary_str())
print(a.special())
print(a.dulicate())
print(a.uncommon())













































