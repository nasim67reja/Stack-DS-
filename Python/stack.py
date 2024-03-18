# REFERENCE : https://www.geeksforgeeks.org/stack-in-python/

# 3################################ Stack using list
from collections import deque
stack = []

stack.append("a")
stack.append("b")
stack.append("c")

#  after adding element in stack
# print(stack)

stack.pop()
stack.pop()
stack.pop()

# After removing
# print(stack)


# 3################################ Stack using deque modul


stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

# print("stack using deque", stack)

stack.pop()
stack.pop()
stack.pop()
# print("stack using deque", stack)


# 3################################ Createing stack using python list


class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items.
        self.items = []

    def is_empty(self):
        # Return True if the stack is empty, False otherwise.
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack.
        # Raise an exception if the stack is empty.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item of the stack without removing it.
        # Raise an exception if the stack is empty.
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack.
        return len(self.items)


firstSt = Stack()

firstSt.push(1)
firstSt.push("nasim")
firstSt.pop()
firstSt.push(2)
print(firstSt.peek())


# while (not firstSt.empty()):
#     print(firstSt.peek())
#     firstSt.pop()
