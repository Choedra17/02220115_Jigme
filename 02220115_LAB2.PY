
class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0  

    def append(self, element):
        new_node = Node(element)  
        if not self.head: 
            self.head = new_node  
            self.tail = new_node  
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.size= self.size + 1 
        print(f"Appended {element} to the list")

    def get(self, index):
        first_element=self.head
        print(f"Element at index {index}: {first_element.data}")
    
    def set(self,index, element):
        print(f"Set element at {index} to {element}")
    
    def new_size(self): 
        print(f"Current size: {self.size}")

    def prepend(self,element):
        new_node = Node(element)
        if not self.head:  
            self.head = new_node
            self.tail = new_node  
        else:
            new_node.next = self.head  
            self.head = new_node  
        self.size = self.size+1
        print(f"Prepend {element} to the list")

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))  
            current = current.next
        print(f"Print Linked list: [{ ' '.join(elements) }]")
        
        
linked_list = LinkedList()  
linked_list.append(5) 
linked_list.get(0) 
linked_list.set(0,10)
linked_list.new_size()
linked_list.prepend(10)
linked_list.print_list()







