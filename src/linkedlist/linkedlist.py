class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        current_node = self.head
        msg = ""
        while current_node:
            msg = msg + f"{current_node.value} -> "
            current_node = current_node.next
        
        return msg + "None"

    def length(self):
        cont = 0
        current_node = self.head
        while current_node:
            cont = cont + 1
            current_node = current_node.next
        return cont
    
    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_head(self):
        self.head = self.head.next

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        
        return False

    def insert_at(self, value, idx):
        if idx < 0:
            raise ValueError("idx must be a non-negative integer.")
        elif idx == 0:
            self.insert_at_head(value)
        else:
            new_node = Node(value)
            current_node = self.head
            idx_node = 1
            while idx_node <= (idx-1):
                current_node = current_node.next
                idx_node = idx_node + 1

            try:
                new_node.next = current_node.next
                current_node.next = new_node
            except:
                raise ValueError("idx must be at most the number of nodes of the list.")
    
    def delete_at(self, idx):
        if idx < 0:
            raise ValueError("idx must be a non-negative integer.")
        elif idx == 0:
            self.insert_at_head()
        else:
            idx_cont = 0
            current_node = self.head
            prev = None
            while current_node and (idx_cont < idx):
                prev = current_node
                current_node = current_node.next
                idx_cont = idx_cont + 1
            try:
                prev.next = current_node.next
            except:
                raise ValueError("idx must be at most the number of nodes of the list.")