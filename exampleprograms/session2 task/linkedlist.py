#Linked Lists 

#Objective: Implement a singly linked list. 

#Concept: Customer Service Ticketing System. 

#Tasks: 

#Create a Node class. 

#Implement insertion, deletion, and search operations for customer tickets. 

#Multiple tokens for a user are not allowed. 

#Add properties for ticket status and priority. 


class Node:
    def __init__(self, ticket_number, customer_name, status, priority):
        self.ticket_number = ticket_number
        self.customer_name = customer_name
        self.status=status
        self.priority=priority
        self.next=None

class TicketingSystem:
    def __init__(self):
        self.head = None

    def insert_ticket(self, ticket_number, customer_name, status, priority):
        new_ticket = Node(ticket_number, customer_name, status, priority)
        if self.head is None:
            self.head = new_ticket
        else:
            
            current = self.head
            while current.next:
                if current.customer_name == customer_name:
                    raise ValueError("Customer already has a ticket")
                current = current.next
            current.next = new_ticket

    def delete_ticket(self, ticket_number):
        if self.head is None:
            raise ValueError("Ticket list is empty")
        elif self.head.ticket_number == ticket_number:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.ticket_number == ticket_number:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError("Ticket not found")

    def search_ticket(self, customer_name):
        current = self.head
        while current:
            if current.customer_name == customer_name:
                return current.ticket_number
            current = current.next
        return None

ticket_system = TicketingSystem()

ticket_system.insert_ticket(1, "John", "Available", "High")
ticket_system.insert_ticket(2, "Alice", "Available", "Low")
ticket_system.insert_ticket(3, "Bob", "Available", "Medium")

print("Search for John's ticket:", ticket_system.search_ticket("John"))
print("Search for Alice's ticket:", ticket_system.search_ticket("Alice"))
print("Search for Bob's ticket:", ticket_system.search_ticket("Bob"))
try:
    ticket_system.insert_ticket(4, "John", "Available", "High")
except ValueError as e:
    print("Error:", e)

ticket_system.delete_ticket(2)
print("Search for Alice's ticket after deletion:", ticket_system.search_ticket("Alice"))
