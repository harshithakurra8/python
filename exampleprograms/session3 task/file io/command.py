import atexit
from fileio  import read_phonebook_from_json, write_phonebook_to_json

PHONEBOOK_FILE = 'phonebook.json'

def main():
    # Load the phonebook from the JSON file at startup
    phonebook = read_phonebook_from_json(PHONEBOOK_FILE)
    print("Phonebook loaded.")

    # Your application logic here
    # For example, adding a new entry:
    def add_entry(name, phone_number):
        phonebook[name] = phone_number
        print(f"Added {name}: {phone_number}")

    # Example usage of adding an entry
    add_entry('John Doe', '123-456-7890')

    # Function to save the phonebook to the JSON file on exit
    def save_phonebook():
        write_phonebook_to_json(phonebook, PHONEBOOK_FILE)
        print("Phonebook saved.")

    # Register the save function to be called on exit
    atexit.register(save_phonebook)

if __name__ == "__main__":
    main()
