class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def printQueue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0


q = Queue()

q.push('a')
q.push('b')
q.push('c')

print(q.front())
q.printQueue()

q.pop()
q.pop()
q.pop()


print(q.empty())
