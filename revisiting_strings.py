#Use of slashes in strings
msg="John\'s Book"
print(msg)

msg="Content\nMore Content"
print(msg)

msg= "def fire: \n\t print('something') \n\t print('nothing')"
print(msg)


#persent string substitution
name="Joe"
age=21
msg=name + " is " + str(age) + "!"   #string concatenation
print(msg)



#String .format() method

name="john"
age=24
msg="{} is {}!".format(name,age)
print(msg)


name="john"
age=24
msg="{1} is {0}!".format(name,age)    #we use positional arguments here through indexing
print(msg)

name="john"
age=24
msg="{name} is {age}!".format(age=age,name=name)     #we use keyword arguments to position like this 
print(msg)

#Formatted strings

name="Dale"
age=28
msg=f"{name.upper()} is {age}!"    #to create a formatted string with prefix f
print(msg)

#example
tmpl="{name} is {age}!"
print(tmpl.format(name="joe",age=23))
print(tmpl.format(name="jake",age=28))


#string format specifiers
counter=0
while counter!=2:
    counter+=1
    print(f"counter is {counter}")

counter=0
while counter!=2:
    counter+=1
    print(f"{counter=}")


q=143/7
print(f"Quiotient is {q}")

q=143/7
print(f"Quotient is {round(q,2)}")

num=1000000
print(f"{num:,}")

num=1000000
print(f"{num*4:,}")


#Test Alignment Format Specifier(Alignment Spec)

data={
    "joe":8968,
    "Daniel":8679,
    "harika":8889
}

for name in data:
    print(f"{name:>8}{data[name]:>8}")


#Generate multiplication
for i in range(1, 11):
    result = 15 * i
    print(f"15 x {i} = {result}")






