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