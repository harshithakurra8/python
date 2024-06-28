
# Stacks 

#Objective: Implement a stack using a list. 

#Concept: Browser History. 

#Tasks: 

#Implement push, pop, and peek operations for browser navigation. 

#Implement search from the history for a given URL using for-loop. 

#Overload operators to compare stack sizes.
  
class BrowserHistory():
    def __init__(self):
        self.history = []

    def push(self, url):
        self.history.append(url) #Add a new url in the history

    def pop(self):
        if self.is_empty():     #remove and return the top url from the history
            return None
        return self.history.pop()

    def peek(self):
        if self.is_empty():   #return top url without removing history
            return None
        return self.history[-1]

    def search(self, url):
        for website in reversed(self.history):    #search a history for given url
            if website == url:                    #the loop iterates and reverses the order of list
                return True
        return False

    def is_empty(self):
        return len(self.history) == 0      #check if history is empty

    def __len__(self):               #return all the urls in history
      return len(self.history) 

    def __lt__(self, other):
        return len(self.history) < len(other.history) #Check if the size of this history is less than the size of another.
    

    def __le__(self, other):
        return len(self.history) <= len(other.history) #less than or equal to

    def __eq__(self, other):
        return len(self.history) == len(other.history)   #equal to

    def __ne__(self, other):
        return len(self.history) != len(other.history)   #not equal to

    def __gt__(self, other):
        return len(self.history) > len(other.history)    #greater than size of another

    def __ge__(self, other):
        return len(self.history) >= len(other.history)    #greater or  equal to

history = BrowserHistory()
history.push("https://www.google.com")
history.push("https://www.facebook.com")
history.push("https://www.openai.com")

print("History:", history.history)
print("Peek:", history.peek())
print("Search for 'https://www.google.com':", history.search("https://www.google.com"))

history2 = BrowserHistory()
history2.push("https://www.google.com")            # Creating another history        
history2.push("https://www.google.com")                  
history2.push("https://www.facebook.com")
print("History2:", history2.history)

print("History is smaller than History2:", history < history2)     #Comparing histories
print("History is equal to History2:", history == history2)
