#Recursive Functions
def reduce(num):
    while(num):
        print(num)
        num-=1
reduce(3)
    


def reduce(num):
    print(f"called reduce({num})")
    if num:
     print(f"reducing num by{num - 1 =}")
    reduce(num - 1)
print("[START]calling reduce(3)")
reduce(3)


