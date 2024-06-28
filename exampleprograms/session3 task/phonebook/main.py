#Working with Modules and Packages 

#Objective: Organize the application into modules and packages. 

#Tasks: 

#Create a package structure (phonebook package with commands.py, validators.py, models.py). 

#Use .env to load valid patterns for phone numbers. 

#Use a requirements.txt file for any third-party packages used.



# main.py (or wherever you need to load the patterns)

from phonebook import commands, validators
from phonebook.models import Contact

if __name__ == "__main__":
    phonebook = []

    # Add a contact
    name = "John Doe"
    phone_number = "+123 1234567890"
    if validators.is_valid_phone_number(phone_number):
        new_contact = commands.add_contact(phonebook, name, phone_number)
        print(f"Added contact: {new_contact}")
    else:
        print("Invalid phone number")

    # List contacts
    print("Phonebook contacts:")
    for contact in commands.list_contacts(phonebook):
        print(Contact)

    # Remove a contact
    removed_contact = commands.remove_contact(phonebook, name)
    if removed_contact:
        print(f"Removed contact: {removed_contact}")
    else:
        print("Contact not found")