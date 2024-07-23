class Node:
    
    def _init_(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    
    def _init_(self):
        self.head = None
        
    def Print_LL(self):
        n = self.head
        
        if n == 0:
            print("Empty list ")
        
        else:
            while n!= 0:
                print(n.data)
                n = n.ref
                
LL1 = LinkedList()            
LL1.Print_LL()