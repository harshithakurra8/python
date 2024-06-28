#Write a program to implement arrays:
#a. Create Arrays: - Create arrays to store strings, integers, and boolean values.
#b. Insert and Delete Operations:
#- Perform insert and delete operations on each array.
#- Ensure that the string array only accepts string values, the integer array only accepts integer values, and the boolean array only accepts boolean values. Implement exception handling to enforce these constraints.
#- Every time a value is inserted into any of these arrays, it should also be added to a global array.
#c. Search Operation: - Perform a search operation on the global array to retrieve only string, integer, or boolean values from it.
#d. String Matching with Numbers: - Search for numbers in the string array that exist in the integer array. Use the re library for this task.
#e. Remove Values from Global Array: - Remove values from the global array that are present in the respective string, integer, or boolean arrays.


class ArrayManagement():
    def __init__(self):                                                             #__init__ private
        self.string_array = []
        self.integer_array = []
        self.boolean_array = []
        self.global_array = []

    def insert_string(self, val):
        try:
            self.string_array.append(val)
            self.global_array.append(val)
        except KeyError:
            self.string_array.remove(val)
            self.global_array.remove(val)
    def delete_string(self,val):
        self.string_array.remove(val)
        self.global_array.remove(val)

    def insert_integer(self, val):
        try:
            self.integer_array.append(val)
            self.global_array.append(val)
        except KeyError:
            self.integer_array.remove(val)
            self.global_array.remove(val)
    def delete_integer(self,val):
        self.integer_array.remove(val)
        self.global_array.remove(val)

    def insert_boolean(self, val):
        try:
            self.boolean_array.append(val)
            self.global_array.append(val)
        except KeyError:
            self.boolean_array.remove(val)
            self.global_array.remove(val)
    def delete_boolean(self,val):
            self.boolean_array.remove(val)
            self.global_array.remove(val)

    def search_string(self):
        return [val for val in self.global_array if isinstance(val, str)]

    def search(self, manager):
        if manager == str:
            return [val for val in self.global_array if isinstance(val, str)]
        elif manager == int:
            return [val for val in self.global_array if isinstance(val, int)]
        elif manager == bool:
            return [val for val in self.global_array if isinstance(val, bool)]
        else:
            return []

    def string_matching_numbers(self):
        return [str(n) for n in self.integer_array if str(n) in self.string_array]

    def remove_from_global(self, arr_input):
        for val in arr_input:
            if val in self.global_array:
                self.global_array.remove(val)

# Example :
management = ArrayManagement()

# Insert operations
management.insert_string("hello")
management.insert_integer(42)
management.insert_boolean(True)

# Delete operations
management.delete_string("hello")
management.delete_integer(42)
management.delete_boolean(True)

# Search operation
print(management.search(str))  
print(management.search(int))  
print(management.search(bool)) 

# String matching with numbers
print(management.string_matching_numbers())  

# Remove values from global array
management.remove_from_global(["hello", 42, True])
print(management.global_array)  

#Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in Python.

#The isinstance() function returns True if the specified object is of the specified type, otherwise False.

#If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

#__init__ having two underscores is (private)
