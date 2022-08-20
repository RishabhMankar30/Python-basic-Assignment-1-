#1. Write a Python program to check if the given number is a Disarium Number?
def check_disarium(num):
    sum=0
    power=1
    num=str(num)
    for i in num:
        sum=sum+int(i)**power
        power=power+1
    if sum==int(num):
        return "The Number is a Disarium"
    else:
        return "The Number is NOT a Disarium"

print(check_disarium(175))

print(check_disarium(25))
print("---------------------------------------------------------------------------------------------------------------")

#2. Write a Python program to print all disarium numbers between 1 to 100?
def disarium_1_100_():
    l=[]
    for i in range(1, 101):
        num = str(i)
        sum = 0
        power = 1
        for i in num:
            sum = sum + int(i) ** power
            power = power + 1
        if sum == int(num):
            l.append(int(num))
    return "The list of disarium numbers={}".format(l)

print(disarium_1_100_())

print("---------------------------------------------------------------------------------------------------------------")

#3. Write a Python program to check if the given number is Happy Number?
def isHappyNumber(num):
    rem = sum = 0

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


num = 72
result = num

while (result != 1 and result != 4):
    result = isHappyNumber(result)

# Happy number always ends with 1
if (result == 1):
    print(str(num) + " is a happy number")
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif (result == 4):
    print(str(num) + " is not a happy number")

print(isHappyNumber(82))
print("---------------------------------------------------------------------------------------------------------------")
#4. Write a Python program to print all happy numbers between 1 and 100?
def isHappyNumber(num):
    rem = sum = 0

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


# Displays all happy numbers between 1 and 100
print("List of happy numbers between 1 and 100: ")
for i in range(1, 101):
    result = i

    # Happy number always ends with 1 and
    # unhappy number ends in a cycle of repeating numbers which contains 4
    while (result != 1 and result != 4):
        result = isHappyNumber(result)

    if (result == 1):
        print(i),
        print(" ")
print("---------------------------------------------------------------------------------------------------------------")
#5. Write a Python program to determine whether the given number is a Harshad Number?

def check_harshad(num):
    sum=0
    for i in str(num):
        sum=sum+int(i)
    if int(num)%sum==0:
        return"The {} is a Harshad Number".format(num)
    else:
        return "The {} is NOT a Harshad Number".format(num)

print(check_harshad(21))

print(check_harshad(156))

print(check_harshad(545))
print("---------------------------------------------------------------------------------------------------------------")

#6. Write a Python program to print all pronic numbers between 1 and 100?
def pronic_number_1_100():
    l=[]
    for i in range(1,101):
        num=i
        for j in range(1, num + 1):
            if j*(j+1)==num:
                l.append(num)
    return "The list of pronic numbers:",l

# pronic number is a number whose multiplication is multiplication of any two consecative number.
# 6=2*3  #2 and3 are consecutive numbers.
# but this can be use for the numbers less than 6, because
# if we will "multiply two consecative number after 6", we will always get more than 6 of their multiplication value.
# hence by solving this remember that check multiplication of two consecutive number<6
# or  solving this remember that check two consecutive number< number to be check.

print(pronic_number_1_100())


