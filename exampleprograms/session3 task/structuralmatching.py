import re

def validate_phone_number(phone_number):
    # Define a regular expression pattern for phone numbers
    pattern = r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"   #The pattern matches following digits and literal characters 
    return bool(re.match(pattern, phone_number))

def handle_command(command, *args):
    match command:
        case 'add':
            if len(args) == 2:
                name, phone_number = args
                if validate_phone_number(phone_number):
                    return f"Adding {name} with phone number {phone_number}"
                else:
                    return "Invalid phone number format"
            else:
                return "Invalid number of arguments for add command"
        
        case 'search':
            if len(args) == 1:
                name = args[0]
                return f"Searching for {name}"
            else:
                return "Invalid number of arguments for search command"
        
        case 'delete':
            if len(args) == 1:
                name = args[0]
                return f"Deleting {name}"
            else:
                return "Invalid number of arguments for delete command"
        
        case 'list':
            return "Listing all entries"
        
        case _:
            return "Unknown command"

commands = [
    ("add", "Harry", "(123) 456-7890"),
    ("add", "Danny", "123-456-7890"),
    ("search", "John"),
    ("delete", "Joe"),
    ("list"),
    ("add", "Invalid Number", "1234567890"),
    ("unknown")
]

for command in commands:
    print(handle_command(*command))
