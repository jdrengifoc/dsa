class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head:
            self.next = self.head