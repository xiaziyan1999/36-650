class Queue:
    inner_list = []
    top = 0
    
    def enqueue(self, value):
        self.inner_list.insert(self.top, value)
        self.top = self.top + 1

    def dequeue(self):
        value = self.inner_list.pop(0)
        self.top = self.top - 1
        return value
    
    
    def delete(self,data):
        tmp_list=self.inner_list
        for i in range(len(tmp_list)):
            tmp=self.dequeue()
            if tmp!=data:
                self.enqueue(tmp)
                