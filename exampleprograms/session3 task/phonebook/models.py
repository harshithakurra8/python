class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"Contact(name={self.name}, phone_number={self.phone_number})"

    