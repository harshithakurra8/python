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

match command.split():
    case "ls":
        print("Listing directories!")
    case ["ls", flag] if flag in flags:
        print("Listing Directories"
              "with more info!\nwith flag", flag)
    case["ls",dir]:
        print(f"Listing directory {dir}.. ")
        