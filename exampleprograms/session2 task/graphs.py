class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, user1, user2):
        if user1 not in self.adj_list:
            self.adj_list[user1] = []
        if user2 not in self.adj_list:
            self.adj_list[user2] = []
        self.adj_list[user1].append(user2)
        self.adj_list[user2].append(user1)

    def remove_edge(self, user1, user2):
        if user1 in self.adj_list and user2 in self.adj_list[user1]:
            self.adj_list[user1].remove(user2)
        if user2 in self.adj_list and user1 in self.adj_list[user2]:
            self.adj_list[user2].remove(user1)

    def search(self, user1, user2):
        return user1 in self.adj_list and user2 in self.adj_list[user1]

    def find_connections(self, user):
        if user in self.adj_list:
            return self.adj_list[user]
        return []

social_network = Graph()

# Add edges (connections)
social_network.add_edge("Harry", "Bob")
social_network.add_edge("Harry", "Charlie")
social_network.add_edge("Bob", "Danil")
social_network.add_edge("Charlie", "Peter")

# Search for a connection
print(social_network.search("Harry", "Bob"))  # Output: True
print(social_network.search("Harry", "Danil"))  # Output: False

# Find all connections for a user
print(social_network.find_connections("Harry"))  # Output: ['Bob', 'Charlie']
print(social_network.find_connections("Bob"))  # Output: ['Harry', 'Danil']

# Remove an edge (connection)
social_network.remove_edge("Harry", "Bob")
print(social_network.search("Harry", "Bob"))  # Output: False
print(social_network.find_connections("Harry"))  # Output: ['Charlie']
