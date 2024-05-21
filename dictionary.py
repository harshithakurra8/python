#Dictionary or hash tables

{"Joe":879809}
print(hash("joe"))

#Simple Namespace
from types import SimpleNamespace
dale=SimpleNamespace(name="Dale",age=27)
print(dale.age)

from types import SimpleNamespace
dale=SimpleNamespace(name="Dale",age=27)
dale.weight=55
print(dale)


#Named Tuple
from collections import namedtuple
Person=namedtuple("Person",("name","age"))
dale=Person("Dale",27)
print(dale.name)

#items() method

contacts={
    "Joe" :8367,
    "Kim":8899,
    "Harry":9868
    }
for name ,info in contacts.items():
    print(name,info)

 #data
store = {
#    name        price
    "Curd"     : 7.8, 
    "Cake"     : 3.1,
    "Chocolate": 7.9, 
    "Egg"      : 5.8,
    "Bread"    :  1, 
    "Milk"     : 2.5,
    "Corn"     :  2, 
    "Chips"    : 1.5
}

purchased = {
#   name    quantity 
    "Egg"  :    8,
    "Bread":    1,
    "Cake" :    7,
    "Curd" :    2,
    "Corn" :    6
}

print(f"{'Name':<8}{'Price':<8}{'Qty.':>8}{'Amount':>8}")
print('-'*32)

subTotal = 0

for product, quantity in purchased.items():
    price = store.get(product, 0)
    amount = price*quantity
    subTotal+= amount
    print(f"{product:<7} {price:<7} {quantity:>7} {amount:>7}")

print('-'*32)
print(f"{'Subtotal:':<16}{subTotal:>16}")
