class Node:
    def __init__(self):
        self.next = None
        self.data = None
    
    def set_data(self, data):
        self.data = data


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list to the end of it
    def insert(self, data):
        node = Node()
        node.set_data(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
            
    def remove_dups(self):
        current = self.head
        previous = None
        seen = set()

        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

# Driver code - Delete it while writing the tests.  

first_node = Node()
first_node.set_data(11)
linked_list = LinkedList(first_node)
 
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()