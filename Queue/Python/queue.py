

# ########################################################################
# ################## 👉👉👉👉👉 Queue Using python list #####################

# ########################################################################


from collections import deque
queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print(f'After Appending => {queue}')

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(f'After removing => {queue}')

print(f'Size => {len(queue)}')


# ########################################################################
# ################## 👉👉👉👉👉 Queue Using python deque module #####################

# ########################################################################


q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
