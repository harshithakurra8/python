#FILE  IO

file=open("file.txt")                   #open()
contents=file.read()

print(contents)
file.close()


with open("file.txt") as file:              #read()
    print(file.read())


with open("file.txt") as file:
    read1=file.readline(7)
    print(read1)


with open("file.txt") as file:
    lines=file.readlines()
    print(lines)


with open("file.txt","w") as file:                              #write()
    file.write("me?!")


lines=["Oranges are orange in color ."
       "And Banana is yellow in color."
       ]
with open("file.txt","w") as file:
    file.writelines(lines)