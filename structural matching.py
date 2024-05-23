#Pipe operator in case statements:

match input("Are you sure?(y/n):"):
    case "Y"|"y":
        print("Done!")
    case "N"|"n":
        print("Cancelled")
    case cmd:
        print("Unknown Command!,cmd")

#Pattern matching

command=input(">>>")
match command.split():
    case "ls":
        print("Listing Directories")
    case["mkdir",dirname]:
        print(f"Directory{dirname} created!")
        
command=input(">>>")
match command.split():
    case ["ls"]:
        print("Listing Directories")
    case ["ls",("-l"|"-all")]:
        print("Listing directories with more info!")



command=input(">>>")
match command.split():
    case "ls":
        print("Listing directories!")
    case ["ls", flag] if flag in flag:
        print("Listing Directories"
              "with more info!\nwith flag", flag)
    case["ls",dir]:
        print(f"Listing directory {dir}.. ")
        

command=input(">>>")
match command.split():
    case "ls":
        print("Listing Directories")
    case [cmd]:
        print("Unknown Command cmd", cmd)
    case[cmd,*args]:
        print(f"Unknown Command{cmd}"
              f"called with{args}")
        
#match dictionary

visitor={
    "name":input("Name:"),
    "age":input("Age:")

}

match visitor:
    case{"name":"Mike"}:
        print("Welcome!")


visitor={
    "name":input("Name:"),
    "age":int(input("Age:"))

}
friends={"Joe","Dale"}
match visitor:
    case{"name":name} if name in friends:
             print("Hey Dude!")

visitor={
    "name":input("Name:"),
    "age":int(input("Age:"))

}
friends={"Joe","Dale"}
match visitor:
    case{"name":name} if name in friends:
             print("Hey Dude!")
    case{"age":age} if age>20:
        print("Can drink!")

#match objects

from collections import namedtuple
Person=namedtuple('Person','name','age')

visitor=Person(name=input('Name:') ,
                age=int(input('Age:')))
match visitor:
    case Person(name="Mike"):
        print("Welcome!")
    case Person(name="Sam",age=28):
        print("your room no. is 78")
        

