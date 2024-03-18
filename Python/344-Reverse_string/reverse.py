
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


class Solution:

    def reverseString(self, s):
        st = Stack()

        for item in s:
            st.push(item)
        for i in range(len(s)):
            s[i] = st.peek()
            st.pop()

        return s

    #  Reverse string array using two pointer

    def reverseStringString(self, s):
        ls = list(s)
        s = 0
        e = len(ls)-1

        while (s <= e):
            ls[s], ls[e] = ls[e], ls[s]
            s += 1
            e -= 1

        return ''.join(ls)


str = Solution()

print(str.reverseString(["h", "e", "l", "l", "o"]))
