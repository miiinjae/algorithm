import sys
# from collections import deque

T = int(sys.stdin.readline())
# dq = deque([])
# for i in range(T):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push':
#         dq.append(a[1])
#     elif a[0] == 'pop':
#         if dq:
#             pop = dq.popleft()
#             print(pop)
#         else:
#             print('-1')
#     elif a[0] == 'size':
#         print(len(dq))
#     elif a[0] == 'empty':
#         if dq:
#             print('0')
#         else:
#             print('1')
#     elif a[0] == 'front':
#         if dq:
#             front = dq[0]
#             print(front)
#         else:
#             print(-1)
#     elif a[0] == 'back':
#         if dq:
#             back = dq[-1]
#             print(back)
#         else:
#             print(-1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            delete_head = self.head
            self.head = self.head.next
            self.size -= 1
            return delete_head.data
        else:
            return "-1"

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "-1"

    def peek_back(self):
        if not self.is_empty():
            return self.tail.data
        else:
            return "-1"

    def size(self):
        return self.size

    def is_empty(self):
        return self.head is None

dq = Queue()
for i in range(T):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        dq.enqueue(a[1])
    elif a[0] == 'pop':
        print(dq.dequeue())
    elif a[0] == 'size':
        print(dq.size)
    elif a[0] == 'empty':
        if dq.is_empty():
            print('1')
        else:
            print('0')
    elif a[0] == 'front':
        print(dq.peek())
    elif a[0] == 'back':
        print(dq.peek_back())