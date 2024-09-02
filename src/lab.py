from linkedlist import LinkedList, Stack, Queue

print("Linked List")
ll = LinkedList()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.remove_at_head()
ll.insert_at_tail(4)

ll.insert_at("a", 1)
print(ll)
ll.delete_at(3)
print(ll)

print("Stack")
st = Stack()
print(st)
print(st.pop(), st.len)
st.push(1)
st.push("2")
print(st, st.len)
print(st.pop())
print(st, st.len)

print("Simple Queue")
qe = Queue()
qe.dequeue()
print(qe)
qe.enqueue(1)
qe.enqueue(2)
print(qe)


def linear_search(ls: list, search_value) -> bool:
    for elem in ls:
        if elem == search_value:
            return True
    return False

def binary_search(ls: list, search_value, ascending: bool = True) -> bool:
    """
    :param ls: List in ascending (`ascending`=True) or descending (`ascending`=False) order.
    :param search_value: Value to be searched in the list `ls`.
    :param order: Boolean that determines wheter the list has an ascending or descending order.
    """
    mult = 1 if ascending else -1
    first = 0
    last = len(ls)
    while  first <= last:
        midle = (first + last) // 2
        if ls[midle] == search_value:
            return True
        elif mult * ls[midle] < mult * search_value:
            first = midle + 1
        else:
            last = midle - 1

    return False

ls = [1, 2, 4, 6, 9]
print(binary_search(ls, 2))
print(binary_search(ls[::-1], 2))
print(binary_search(ls[::-1], 2, False))