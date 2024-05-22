#count
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter=count(start=1,step=10)
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter=count(start=1)
for num in counter:
    print(num)
    if num==18:
        break


from itertools import count
counter=count(start=1)
lst=["Milk","Egg","Curd"]
for index, item in zip(counter,lst):
    print(index,item,sep=".")


#cycle()

from itertools import cycle
instructions=("eat","code","sleep")
counter=0
for instruction in cycle(instructions):
    print(instruction)
    counter+=1
    if counter==5:
        break

#repeat()
from itertools import repeat
for msg in repeat("Say Something!",times=3):
    print(msg)

#combinations()
from itertools import combinations
players=["Tom","Dale","Jack"]
for group in combinations(players,2):
    print(group)

#permutations()
from itertools import combinations,permutations
players=["Tom","Jack","Daniel"]
for seats in permutations(players,2):
    print(seats)

#product()
from itertools import product
team_a=["Joe[A]","Kim[A]"]
team_b=["Tom[B]","Harry[B]"]
for pair in product(team_a,team_b):
    print(pair)

from itertools import product
team_a=["Joe[A]","Kim[A]"]
team_b=["Tom[B]","Harry[B]"]
team_c=["Peter[C]","George[C]"]
for pair in product(team_a,team_b,team_c):
    print(pair)

from itertools import product
team_a=["Joe[A]","Kim[A]"]
team_b=["Tom[B]","Harry[B]"]
team_c=["Peter[C]","George[C]"]
for pair in product(team_a,repeat=3):
    print(pair)

#combinations_with_replacement()
from itertools import combinations_with_replacement
colors=["blue","pink","black"]
for mix in combinations_with_replacement(colors,2):
    print(mix)

#chain()
from itertools import chain
gen=(x for x in range(2,10,2))
lst=[12,16,18]
for num in chain(gen,lst):
    print(num)

#islice()
from itertools import islice
gen=(x for x in range(2,10,2))
lst=[12,16,18]
for num in islice(gen,2,5):
    print(num)

#compress()
from itertools import compress
name=["Tom","Jack","Peter"]
adult=[True,False,True]
for adult_name in compress(name, adult):
    print(adult_name)

#filter()
age=[26,27,29,17,30,11,16]
adults=filter(
    lambda age:age>=18,
    age
    )
print([age for age in adults])

#filterFalse()
from itertools import filterfalse
age=[26,27,29,17,30,11,16]
minors=filterfalse(
    lambda age:age>=18,
    age
    )
print([age for age in minors])

#accumulate
from operator import add
from itertools import accumulate
age=[27,26,17,29]
for accu_age in accumulate(age, add):
    print(accu_age)

from operator import sub
from itertools import accumulate
age=[27,26,17,29]
for accu_age in accumulate(age, sub):
    print(accu_age)

#groupby()
from itertools import groupby
people=[
    {'name':'Jack','Adult':False},
    {'name':'Joe','Adult':True},
    {'name':'Peter','Adult':False},
    {'name':'Harry','Adult':True},
    {'name':'Kim','Adult':False}
]
adult_select=lambda person: person['Adult']
for group in groupby(people,adult_select):
    print(group)

from itertools import groupby
people=[
    {'name':'Jack','Adult':False},
    {'name':'Joe','Adult':True},
    {'name':'Peter','Adult':False},
    {'name':'Harry','Adult':True},
    {'name':'Kim','Adult':False}
]
adult_select=lambda person: person['Adult']
for group in groupby(people,adult_select):
    print("Adult" if group[0] else "Minor")
    print([person['name']
           for person in group[1] ])
    print(group)