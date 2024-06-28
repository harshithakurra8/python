 #Hash Tables 

#Objective: Implement a basic hash table. 

#Concept: User Login System. 

#Tasks: 

#Implement insertion, deletion, and search operations for user credentials. 

#Use exception handling for invalid operations.


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def _hash(self, key):
        return hash(key) % self.size  # Calculate hash value for given key (username)

    def insert(self, username, password):
        index = self._hash(username)
        for entry in self.table[index]:
            if entry[0] == username:
                raise ValueError("Username already exists")
        self.table[index].append((username, password))

    def delete(self, username):
        index = self._hash(username)
        for entry in self.table[index]:
            if entry[0] == username:
                self.table[index].remove(entry)
                return
        raise ValueError("Username not found")

    def search(self, username):
        index = self._hash(username)
        for entry in self.table[index]:
            if entry[0] == username:
                return entry[1]
        raise ValueError("Username not found")

    def login(self, username, password):
        try:
            stored_password = self.search(username)
            if stored_password == password:
                print(f"User '{username}' logged in successfully.")
            else:
                raise ValueError("Incorrect password")
        except ValueError as e:
            print(f"Login failed: {e}")

hash_table = HashTable(10)

try:
    hash_table.insert("user1", "password1")
    hash_table.insert("user2", "password2")
    print(f"user1's password: {hash_table.search("user1")}")                      
    hash_table.login("user1", "password1")  
    hash_table.login("user1", "wrongpassword")  
    hash_table.delete("user2")
    hash_table.login("user2", "password2")  

except ValueError as e:
    print("Error:", e)
