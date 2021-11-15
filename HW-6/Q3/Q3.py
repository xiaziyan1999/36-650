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
        
        
        
    def sortList(self):
        tmp=[]
        current=self.head
        while current != None:
              tmp.append(current.data)
              current=current.next
        for i in range(len(tmp)):
            for j in range(0, len(tmp)-i-1):
                if tmp[j] > tmp[j+1] :
                    temp = tmp[j]
                    tmp[j] = tmp[j+1]
                    tmp[j+1] =  temp
        current=self.head
        for k in range(len(tmp)):
            current.data=tmp[k]
            current=current.next