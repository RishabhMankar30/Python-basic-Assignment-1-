#Question1:
def amplify(num):
    l=[]
    for i in range(1,num+1):
        if i%4==0:
            amp=i*10
            l.append(amp)
        else:
            l.append(i)
    return l

print(amplify(4))
print(amplify(3))
print(amplify(25))
print("--------------------------------------------------------------------------------------------------------------")

#Question2:

def unique(l):
    if type(l)==list:
        l1=[]
        for i in l:
            c=l.count(i)
            if c==1:
                l1.append(i)
        return l1

print(unique([3, 3, 3, 7, 3, 3]))
print(unique([0, 0, 0.77, 0, 0]))
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))
print("----------------------------------------------------------------------------------------------------------------")

#Question3:
class circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        area=3.1415*(self.radius**2)
        return area
    def get_perimeter(self):
        peri=2*3.1415*self.radius
        return peri

circy=circle(11)
print(circy.get_area())

circy=circle(4.44)
print(circy.get_perimeter())

print("----------------------------------------------------------------------------------------------------------------")

#Question4:
#method no1:
def sort_by_length(l):
    sorted_list=sorted(l,key=len)
    return sorted_list

l1=["Google", "Apple", "Microsoft"]
print(sort_by_length(l1))
l2=["Leonardo", "Michelangelo", "Raphael", "Donatello"]
print(sort_by_length(l2))
l3=["Turing", "Einstein", "Jung"]
print(sort_by_length(l3))

#Method No2:
def sorting_according_length(l):
    length_list=[] # in this list, we will put the length of each character in list l but sorted wise.
    sorted_charcter_list=[]
    for i in l:
        length_list.append(len(i))
    length_list.sort()
    for num in length_list:
        for chr in l:
            if len(chr)==num:
                sorted_charcter_list.append(chr)
    return sorted_charcter_list

l1=["Google", "Apple", "Microsoft"]
print(sorting_according_length(l1))
l2=["Leonardo", "Michelangelo", "Raphael", "Donatello"]
print(sorting_according_length(l2))
l3=["Turing", "Einstein", "Jung"]
print(sorting_according_length(l3))
print("----------------------------------------------------------------------------------------------------------------")

#Question5:
def is_triplet(n1,n2,n3):
    l=[n1,n2,n3]
    l.sort() #sorting the list in ascending order, smallest to largest.
    sq_of_2smallest=(l[0]**2)+(l[1]**2)
    sq_of_largest=l[2]**2
    if sq_of_2smallest==sq_of_largest:
        return "True"
    else:
        return "False"

print(is_triplet(3,4,5))
print(is_triplet(13,5,12))
print(is_triplet(1,2,3))








