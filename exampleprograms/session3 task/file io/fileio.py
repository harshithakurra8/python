#File I/O
#•	Objective: Read and write phonebook entries to JSON files.
#•	Tasks:
#1.	Implement functions to read from and write to a JSON file.
#2.	Ensure that the phonebook is loaded from the file on startup and saved to the file on exit.

import json

def read_phonebook_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            phonebook = json.load(file)
        return phonebook
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def write_phonebook_to_json(phonebook, file_path):
    with open(file_path, 'w') as file:
        json.dump(phonebook, file, indent=4)
