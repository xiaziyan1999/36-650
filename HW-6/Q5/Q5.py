class Node(object):
    def __init__(self):
        self.data = None
        self.next=None
        
    def set_data(self,data):
        self.data = data
        self.next=None
        


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

    # Insert a node in a linked list
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

            tmp1 = None
            tmp2 = None
            dup = None
            tmp1 = self.head
            while (tmp1 != None and tmp1.next != None):
                tmp2 = tmp1
                while (tmp2.next != None):
                    if (tmp1.data == tmp2.next.data):
                        dup = tmp2.next
                        tmp2.next = tmp2.next.next
                    else:
                        tmp2 = tmp2.next
                tmp1 = tmp1.next