class Node:
    def _init_(self,data):
        self.pref = None
        self.data = data 
        self.nref = None
        
class D_ll:
    
    def __init__(self):
        self.head = None
        
    def print_ll(self):
        
        if self.head == None:
            print("List is empty ")
        
        else:
            n = self.head
            
            while n.pref != None:
                print(n.data , "--> " , end=" ")
                
    def print_dll(self):
        
        if self.head == None:
            print("List is Empty ")
            
        else:
            
            n = self.head 
            
            while n.nref != None:
                print(n.data, "--> " , end=" ")
                n = n.nref
                
                while n.pref != None:
                    print(n.data, "---> " , end=" ")
                    n = n.pref
                    
dd1 = D_ll()
dd1.print_dll()
            