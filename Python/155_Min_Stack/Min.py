class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        min = self.items[0]
        for item in self.items:
            if (item < min):
                min = item
        return min


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  # return -3
minStack.pop()
minStack.top()   # return 0
minStack.getMin()  # return -2
