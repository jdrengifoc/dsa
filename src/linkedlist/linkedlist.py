class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __str__(self) -> str:
        current_node = self.head
        msg = ""
        while current_node:
            msg = msg + f"{current_node.value} -> "
            current_node = current_node.next
        
        return msg + "None"

    def length(self) -> int:
        cont = 0
        current_node = self.head
        while current_node:
            cont = cont + 1
            current_node = current_node.next
        return cont
    
    def insert_at_head(self, value) -> None:
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def insert_at_tail(self, value) -> None:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_head(self):
        self.head = self.head.next

    def search(self, value) -> bool:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        
        return False

    def insert_at(self, value, idx: int) -> None:
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
    
    def delete_at(self, idx: int) -> None:
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
            

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.len = 0

    def __str__(self) -> str:
        current_node = self.top
        msg = "Top: "
        while current_node:
            msg = msg + f'{current_node.value} -> '
            current_node = current_node.next
        
        return msg + 'None'

    def push(self, value) -> None:
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.len += 1

    def pop(self):
        if self.top is None:
            return None
        else:
            prev_top = self.top
            self.top = self.top.next
            prev_top.next = None
            self.len -= 1
            return prev_top.value
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None
        
class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        current_node = self.head
        msg = "head: "
        while current_node:
            msg = msg + f"{current_node.value} -> "
            current_node = current_node.next
        return msg + "None"
    
    def enqueue(self, value) -> None:
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current_head = self.head
            self.head = current_head.next
            current_head.next = None
            if self.head is None:
                self.tail = None



