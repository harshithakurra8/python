#: Iterators and Generators
#•	Objective: Implement list comprehensions, generators, and use the itertools module.
#•	Tasks:
#1.	Use list comprehensions to filter and transform phonebook entries.
#2.	Implement a generator to iterate over phonebook entries.
#3.	Use itertools to perform advanced operations like grouping

phonebook = {
    "Alice": "123-456",
    "Bob": "789-012",
    "Charlie": "345-678",
    "David": "901-234"
}

# Filter phonebook entries to include only names starting with 'A'
filtered_entries = {name: number for name, number in phonebook.items() if name.startswith('A')}
print("Filtered Entries:", filtered_entries)

# Transform phone numbers to include country code
transformed_numbers = {name: f"+1-{number}" for name, number in phonebook.items()}
print("Transformed Numbers:", transformed_numbers)

def phonebook_generator(phonebook):
    for name, number in phonebook.items():
        yield name, number

# Using the generator to iterate over phonebook entries
for name, number in phonebook_generator(phonebook):
    print(f"{name}: {number}")

import itertools

# Group phonebook entries by name length
grouped_entries = itertools.groupby(sorted(phonebook), key=lambda x: len(x))
for key, group in grouped_entries:
    print(f"Names with length {key}: {[name for name in group]}")
