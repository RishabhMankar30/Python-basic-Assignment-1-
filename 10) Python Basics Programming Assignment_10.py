import logging
logging.basicConfig(filename="assi_10",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
logging.info("we are solving python basic programming assigement_10")

class assign_10:
    # 1. Write a Python program to find sum of elements in list?
    def list_sum(self,l):
        try:
            logging.info("we are finding sum of all the element in the list")
            if type(l)==list:
                logging.info("the given list is--->%s",l)
                sum=0
                for i in l:
                    sum=sum+i
                logging.info("the sum of all the elementis ---> %s",sum)
                return "the sum of all the element in a list= {}".format(sum)

        except Exception as e:
            logging.exception(e)
    #2. Write a Python program to Multiply all numbers in the list?
    def list_mul(self,l):
        try:
            logging.info("We are finding the multiplication of all the digit in a list")
            if type(l)==list:
                logging.info("the given list is--->%s",l)
                mul=1
                for i in l:
                    mul=mul*i
                logging.info("the multiplication of all the element in a list is----> %s",mul)
                return "the multiplication of all the element in a list= {}".format(mul)
        except Exception as e:
            logging.exception(e)

    #3. Write a Python program to find smallest number in a list? [we can also use inbuilt function "min(list)"]
    def list_small(self,l):
        logging.info("We are finding the smallest no. in a given list")
        try:
            if type(l)==list:
                logging.info("the given list is--->%s", l)
                small=l[0]
                logging.info("we are iterating through the loop to check the smallest no. in a list")
                for i in l:
                    if i<small:
                        small=i
                logging.info("the smallest no. in a list is ---> %s",small)
                return "the smallest no. in a list= {}".format(small)
        except Exception as e:
            logging.exception(e)

    #4. Write a Python program to find largest number in a list?[we can also use inbuilt function "max(list)"]
    def larg_list(self,l):
        try:
            logging.info("We are finding the largest no. in a list")
            if type(l)==list:
                logging.info("The given list is--->%s",l)
                larg=l[0]
                for i in l:
                    if i>larg:
                        larg=i
                logging.info("the largest no. in a list is---> %s",larg)
                return "The largest no. in a list= {}".format(larg)
        except Exception as e:
            logging.exception(e)


    #5. Write a Python program to find second largest number in a list?
    #method1: By "list.sort()" function in list (this function sort list data by default in accending order)
    def larg_2nd(self,l):
        try:
            logging.info("we are finding the second largest no. in a list")
            if type(l)==list:
                logging.info("The given list is---> %s",l)
                l.sort()
                print("the list after arranging data in accending order= {}".format(l))
                logging.info("the list after arranging data in accending order-->%s",l)
                larg_1st=l[-1]
                larg_2nd=l[-2]
                logging.info("The 1st largest num=%s",larg_1st)
                logging.info("The 2nd largest num=%s",larg_2nd)
                print("The 1st largest num={}".format(larg_1st))
                print("The 2nd largest num={}".format(larg_2nd))

        except Exception as e:
            logging.exception(e)

    #method2: By max(list) inbuilt function can also be solve

    #6. Write a Python program to find N largest elements from a list?
    def Nth_largest(self,l):
        logging.info("we are finding a  N largest elements from a list")
        try:
            if type(l) == list:
                logging.info("the list is---> %s", l)
                print("the lenth of the list is= {}".format(len(l)))
                logging.info("The lenth of list-->%s",len(l))
                N = int(input("Enter which largest number you want (like 1st,2nd largest etc) but number should be within length of list: "))
                l.sort()  # this will sort the given list in accending order by default(for deccending order list.sort(reverse=True)
                Nth_largest = l[-N]
                logging.info("The %s th largest number in a list is---> %s", N, Nth_largest)
                return "The {}th largest number in a list is= {}".format(N, Nth_largest)
        except Exception as e:
            logging.exception(e)

    #7. Write a Python program to print even numbers in a list?
    def even_num(self,l):
        try:
            logging.info("we are here finding the even number in a list")
            if type(l) == list:
                even = []
                logging.info("The given list is---> %s", l)
                for i in l:
                    if i % 2 == 0:
                        even.append(i)
                logging.info("the list of Even number is---> %s", even)
                return "the list of EVEN number={}".format(even)
        except Exception as e:
            logging.exception(e)

    #8. Write a Python program to print odd numbers in a List?
    def odd_num(self,l):
        try:
            logging.info("we are here finding the odd number in a list")
            if type(l) == list:
                odd = []
                logging.info("The given list is---> %s", l)
                for i in l:
                    if i % 2 != 0:
                        odd.append(i)
                logging.info("the list of Even number is---> %s", odd)
                return "the list of ODD number={}".format(odd)
        except Exception as e:
            logging.exception(e)

    #9. Write a Python program to Remove empty List from List?
    def rem_emptylst(self,l):
        logging.info("remove the empty list from a given list ")
        if type(l)==list:
            logging.info("The given list is ---> %s",l)
            for i in l:
                if i==[]:
                    logging.info("we got the empty list-->%s",i)
                    print("Yes! we got the empty list")
                    l.remove(i)
                    logging.info("The list after removing empty list is-->%s",l)
                    return "The list after removing empty list= {}".format(l)
            else:
                logging.info("There is no empty list in the given list!")
                return "There is no empty list in the given list! "

    #10. Write a Python program to Cloning or Copying a list?

    """*There are various ways of copying an list 1)Using the slicing technique 
    2)Using the extend() method, 3) using =(assignment operator), 4)Using the method of Shallow Copy 
    5) Using the method of Deep Copy, 6)Using the copy() method  """
    """*In Python, Assignment statements do not copy objects, 
    they create bindings between a target and an object. When we use = operator user thinks that this creates a new object; well, it doesn’t. 
    It only creates a new variable that shares the reference of the original object. 
    Sometimes a user wants to work with mutable objects, 
    in order to do that user looks for a way to create “real copies” or “clones” of these objects. 
    Or, sometimes a user wants copies that user can modify without automatically modifying the original at the same time, in order to do that we create copies of objects.
    A copy is sometimes needed so one can change one copy without changing the other."""
    #https://www.geeksforgeeks.org/python-cloning-copying-list/
    def copy_lst(self,l):
        logging.info("We are copying or cloning(real copy) the given list")
        try:
            if type(l) == list:
                logging.info("The origional list--->%s", l)
                import copy
                copy_lst = copy.copy(l)
                logging.info("The cloning of origional list is-->%s", copy_lst)
                print("The origional list is={}".format(l))
                print("The cloning of origional list is= {}".format(copy_lst))
        except Exception as e:
            logging.exception(e)

    #11. Write a Python program to Count occurrences of an element in a list?
    def occurance(self,l):
        try:
            logging.info("we are counting the occurance of each element in a list")
            if type(l)==list:
                logging.info("The given list is-->%s",l)
                d={}
                for i in l:
                    count_num=l.count(i)
                    d[i]=count_num
                    logging.info("The number of occurance of element: %s -->element is:%s",i,count_num)
                print("1st digit is element and 2nd digit is its occurance",d)
                return " These are the occurance of all elements"
        except Exception as e:
            logging.exception(e)

a=assign_10()
l=[1,2,6,33,78,54,74,32,11,65,5,3,12,13]
l1=[1,2,6,33,78,[],54,2,74,32,11,65,5,3,12,13]
print(a.list_sum(l))
print(a.list_mul(l))
print(a.list_small(l))
print(a.larg_list(l))
print(a.larg_2nd(l))
print(a.Nth_largest(l))
print(a.even_num(l))
print(a.odd_num(l))
print(a.rem_emptylst(l1))
print(a.copy_lst(l))
print(a.occurance(l))



































