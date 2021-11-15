#1. Create the Data Structure (storage data type and the organizer)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Linked List
class LinkedList(object):
    
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")
        tmp=[]
        current = self.tail
        while current!=None:
            tmp.append(current.data)
            current=current.previous
        for i in range(len(tmp)):
            k= len(tmp)-1-i
            print(tmp[k],end="  ")
        print("\n")
        
        
#2. Create the insert() function
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            while current.previous != None:
                current = current.previous
        current.previous = node

        
#3. Create the delete() function. Predict its behavior from the insertion flow shown above.            
    def delete(self, data):
        if not self.tail:
            return
        temp = self.tail
        if self.tail.data == data:
            head = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return

#4. Create search() function that returns true/false based on if given data point is stored in any of the nodes (i.e. search (12) → true, search (20) → false)   
    def search(self, data):
        current = self.tail
        count=0
        while current!= None:
                if current.data == data:
                    count+=1
                else:
                    count+=0
                current = current.previous
        if count==0:
            print('FALSE')
        else:
            print('TRUE')