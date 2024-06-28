from phonebook.models import Contact

def add_contact(phonebook, name, phone_number):
    new_contact = Contact(name=name, phone_number=phone_number)
    phonebook.append(new_contact)
    return new_contact

def remove_contact(phonebook, name):
    for contact in phonebook:
        if contact.name == name:
            phonebook.remove(contact)
            return contact
    return None

def list_contacts(phonebook):
    return phonebook
