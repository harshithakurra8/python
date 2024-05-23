#is operator
lst1=[0,0]
lst2=[0,0]
lst_copy=lst1
print(lst_copy is lst1)

lst1=[0,0]
lst2=[0,0]
lst_copy=lst1
lst_copy[1]=1
print(lst_copy)

#Shallow and Deep copies
lst=[0 , [1, 1]]
lst_copy=lst.copy()
lst_copy[1][0]="?!"
print(lst)

from copy import deepcopy
lst=[0 , [1, 1]]
lst_copy=deepcopy(lst)
lst_copy[1][0]="?!"
print(lst)

#tuple unpacking
name,age=("Joe",27)
print(name)

#Dictionary Unpacking
friends={
    "Dale":8757,
    "Joe":8777
}
contacts={
    "Jack":8668,
    "John":8757,
    **friends
}
print(contacts)

#Tuple Packing
name,age,weight,is_programmer=(
    "Joe",34,57,False
)
print(is_programmer)

name,*cache,is_programmer=(
    "Joe",34,57,False
)
print(cache)

#Arguments Unpacking
contacts={
    "Joe":8767,
     "Dale":9880
     
}
def add_contacts(name, info):
    contacts[name.capitalize()]=info
    john=("John",67)
    add_contacts(**john)

#Walrus := Operator
print(
    (num:=2)
)

#pipe| operator

friends={
    "joe":8988,
    "Peter":8679
}

kyle={"kyle":6877}

contacts=kyle|friends

print(contacts)

#this also works with update methos

friends={
    "joe":8988,
    "Peter":8679
}

contacts={"kyle":6877}

contacts.update(friends)
contacts|=friends

print(contacts)

#Variable scope
num=0
def change():
    num=1
change()
print(num)


num=0
def change(x):
    x=1
    print(x)
change(0)
print(globals())

globals()['num']=0
input()
def change (x):
    x=1
    print(locals())
change(0)

#Python REPL
name="Dale"

def exclaim():
    return"?!"

def root(num):
    return pow(num,.5)