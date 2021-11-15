#1. Create the data structure (custom data type and the organizer)
class Node(object):
    def __init__(self, data):
        self.toobig = None 
        self.big = None 
        self.small = None
        self.data = data 
        self.arr=[data]
    
 #2. Create the insert() function for this data structure   
    def insert(self, data):
        if (data-self.data)>=10:
            if self.toobig is None:
               self.toobig = Node(data)
            else:
               self.toobig.insert(data)
        elif (data-self.data<10) and (data-self.data>=0 ):
            if self.big is None:
                self.big = Node(data)
            else:self.big.insert(data)
        else:
            if self.small is None:
                self.small = Node(data)
            else:self.small.insert(data)
        self.arr.append(data)                     
    
            
#3. Create the delete () function for this data structure            
    def delete(self,data):
        if not self.data: 
            print ("Tree is incomplete.")
            return None
        tmp=self.arr
        tmp.remove(data)
        self.data=tmp[0]
        self.toobig=None
        self.big=None
        self.small=None
        for i in range(1,len(tmp)):
            self.insert(tmp[i])
            
                        
 #4. Create traversal() function for this data structure.              
    def traversal(self):
            if self.small:
                self.small.traversal()
            print(self.data)
            if self.big:
                self.big.traversal()
            if self.toobig:
                self.toobig.traversal()
