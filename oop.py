#object
print(issubclass(int,object))


#class and instance variable
class Dollar:
    symbol="$"
    def __init__(self,val):
        self.value=val
bill=Dollar(100)
big_bill=Dollar(1000)
print(bill.value!=big_bill.value)

class Dollar:
    symbol="$"
    def __init__(self,val):
        self.value=val
bill=Dollar(100)
big_bill=Dollar(1000)
print(bill.symbol==big_bill.symbol)

class Dollar:
    symbol="$"
    def __init__(self,val):
        self.value=val
bill=Dollar(100)
big_bill=Dollar(1000)
Dollar.symbol="?"
print(bill.symbol)

class Dollar:
    symbol="$"
    def __init__(self,val):
        self.value=val
bill=Dollar(100)
big_bill=Dollar(1000)
bill.symbol="?"
print(big_bill.symbol)

#Create a class Student that should initialize name and age (both given during initialization).

#Create another class Course, which should initialize a title (given during initialization) and a students protected attribute which should be set to an empty list by default. Course should have a total_students() method which should return the total number of students in the students list and an add_student() which should receive a Student object and append it to the students list.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, title):
        self.title = title
        self._students = []

    def total_students(self):
        return len(self._students)

    def add_student(self, student):
        if isinstance(student, Student):
            self._students.append(student)
        else:
            print("Invalid")


class Person:
    def __new__(cls,name):
        print("newly created")
        return super().__new__(cls)
    def __init__(self,name):
        print("initialized")
        self.name=name
Person("Jake")
        
