#list comprehension
lst=[]
for num in range(0,20):
    lst.append(num)
    print(num)

lst=[num for num in range(0,20)]
print(lst)

names=["joe","john","dale"]
lst=[name.capitalize() for name in names]
print(lst)

#If Statement in List Comprehension
def is_even(num):
    return num%2==0
lst=[num 
     for num in range(0,20)
     if is_even(num)]
print(lst)

#Set and Dictionary Comprehension
lst=[x
     for x in range(3)]
for x in range(2):
    for y in range(2):
        print(x,y)

lst=[f"{x} {y}"
     for x in range(3)
     for y in range(3)
     ]
print(lst)

lst={x
     for x in range(3)}
print(lst)

lst={x:x*x
     for x in range(3)}
print(lst)

lst=(x
     for x in range(3))    #generator expression
print(lst)

#Generator

gen=(x for x in range(3))
print(next(gen))
print(next(gen))

def range_even(end):
    for num in range(0, end ,2):
        return num(2)
    print(range_even(6))


def range_even(end):
    for num in range(0, end ,2):
        yield num
for num in range_even(6):
        print(num)

def range_even(end):
    for num in range(0, end ,2):
        print(f"yielding value{num}")
        yield num
for num in range_even(6):
        print(num)


#Chaining Generators

def lengths(itr):
     for ele in itr:
          yield  len(ele)

def hide(itr):
               for ele in itr:
                    yield ele* "*"
passwords={"not good","give m_pass","00100=100"}
for password in hide(lengths(passwords)):
     print(password)

#enumarate() function
lst=["milk","curd","honey"]
for index in range(len(lst)):
     print(f"{index+1}.{lst[index]}")

lst=["milk","curd","honey"]
#for index in range(len(lst)):
    # print(f"{index+1}.{lst[index]}")
for index, item in enumerate(lst, start=1):
          print(f"{index}.{item}")

#Zip()function
name=["Joe","Peter","Harry"]
info=[67,88,78,88]
for nm,inf in zip(name,info):
      print(nm,inf)

#zip_longest()function
from itertools import zip_longest
name=["Joe","Peter","Harry","Daniel"]
info=[67,88,88]
for nm,inf in zip_longest(name,info,fillvalue=0):
      print(nm,inf)

#all()function

lst=[]
while True:
      match input("Add more items?(y/n):"):
          case"y":  
                  item=input("Item:")
                  lst.append(item)
          case"n": 
                  break
print(lst)
                   
lst=[]
while True:
      match input("Add more items?(y/n):"):
          case"y":  
                  item=input("Item:")
                  lst.append(item)
          case"n": 
                  break
if all(lst):
      print(lst)
else:
      print("Something I didn't understand")

#any()function
lst=[0,0,0.1,0]
if any(lst):
      print("it has some value")
else:
      print("useless")