from array import array
num=array("i",(1,2,3,4,5))
print(num)

from array import array
num=array("i",(1,2,3,4,5))
num.append(8)
#len(num)
print (len(num))

#Stack LIFO
from collections import deque
cookies=deque((1,2,3,4))
cookies.appendleft(0)
print(cookies)

from collections import deque
cookies=deque((1,2,3,4))
first_cookie=cookies.popleft()
print(first_cookie)



from queue import LifoQueue
cookies=LifoQueue(maxsize=3)
cookies.put("cookies 3")
cookies.put("cookies 2")
cookies.put("cookies 1")
if not cookies.full():
    cookies.put("cookies 0")
else:
    print("stack is full")

#Queue FIFO

from queue import Queue
q=Queue()
q.put("John")
q.put("Dale")
q.put("Harry")
print(q.get())

from queue import PriorityQueue
q=PriorityQueue()
q.put((88,"Joe"))
q.put((9,"George"))
q.put((99,"Harry"))
print(q.get())


#collections module
from collections import Counter
answers=['not answered','wrong','answered','answered','answered','answered','answered',
         'not answered','answered','wrong','answered']
counted_ans=Counter(answers)
print (counted_ans)

from collections import defaultdict
store=defaultdict(float)
store["Milk"]=5.75
store["banana"]=8.79
store["paper"]
print(store)

#Sorting Arrays with Non-Numerical Data
#Sort the given lst in ascending order and then print it.


lst = ["10 Min", "5 Min", "2 Min", "9 Min", "14 Min"]
def sorter(ele):
    num = ele.split()[0]
    return int(num)
lst.sort(key=sorter)


