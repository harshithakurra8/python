 #Trees (Binary Search Tree) 

#Objective: Implement a binary search tree (BST). 

#Concept: Contact Directory. 

#Tasks: 

#Implement insertion, deletion, and search operations for contacts. 

#Use properties for contact name and phone number.

class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None
class ContactBST:
    def __init__(self):
        self.root = None
    
    def insert(self, name, phone):
        if not self.root:
            self.root = ContactNode(name, phone)
        else:
            self._insert(self.root, name, phone)
    
    def _insert(self, node, name, phone):
        if name < node.name:
            if not node.left:
                node.left = ContactNode(name, phone)
            else:
                self._insert(node.left, name, phone)
        elif name > node.name:
            if not node.right:
                node.right = ContactNode(name, phone)
            else:
                self._insert(node.right, name, phone)
        else:
            node.phone = phone                                              
    
    def search(self, name):
        return self._search(self.root, name)
    
    def _search(self, node, name):
        if not node:
            return None
        if name < node.name:
            return self._search(node.left, name)
        elif name > node.name:
            return self._search(node.right, name)
        else:
            return node
    
    def delete(self, name):
        self.root = self._delete(self.root, name)
    
    def _delete(self, node, name):
        if not node:
            return node
        if name < node.name:
            node.left = self._delete(node.left, name)
        elif name > node.name:
            node.right = self._delete(node.right, name)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.name = temp.name
            node.phone = temp.phone
            node.right = self._delete(node.right, temp.name)
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

def in_order_traversal(node):
    if not node:
        return []
    return in_order_traversal(node.left) + [(node.name, node.phone)] + in_order_traversal(node.right)
contact_directory = ContactBST()
contact_directory.insert("Alice", "123-456-7890")
contact_directory.insert("Bob", "234-567-8901")
contact_directory.insert("Charlie", "345-678-9012")
result = contact_directory.search("Alice")
if result:
    print(f"Found: {result.name}, {result.phone}")  
else:
    print("Contact not found")
contact_directory.delete("Bob")
print(in_order_traversal(contact_directory.root))  



    
