from linkedlist import LinkedList, Stack

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
