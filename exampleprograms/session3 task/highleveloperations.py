#High-Level Operations
#•	Objective: Demonstrate tuple packing/unpacking, pointers, variable scope.
#•	Tasks:
#1.	Implement functions that use tuple packing and unpacking.
#2.	Demonstrate variable scope within functions.
#3.	Use pointers (references) to update phonebook entries.

# Tuple packing
def pack_example():
    return 1, 2, 3  # packing into a tuple

# Tuple unpacking
def unpack_example():
    a, b, c = pack_example()  # unpacking the tuple
    print(f"a = {a}, b = {b}, c = {c}")

# Testing tuple packing and unpacking
unpack_example()  # Output: a = 1, b = 2, c = 3

# Global variable
global_var = 10

def scope_example():
    local_var = 5  # Local variable
    print(f"Inside function: local_var = {local_var}, global_var = {global_var}")

scope_example()
print(f"Outside function: global_var = {global_var}")
# print(local_var)  # This will cause an error because local_var is not accessible here

# Using pointers (references) to update phonebook entries (dictionary example)
def update_phonebook(phonebook, name, new_number):
    if name in phonebook:
        phonebook[name] = new_number

# Example usage
phonebook = {"Alice": "123-456", "Bob": "789-012"}
update_phonebook(phonebook, "Bob", "456-789")
print(phonebook)  # Output: {'Alice': '123-456', 'Bob': '456-789'}

