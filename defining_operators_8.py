class Queue:
    def __init__(self, *args):
        self.elements = list(args)

    def append(self, *values):
        self.elements.extend(values)

    def copy(self):
        return Queue(*self.elements)

    def pop(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            return None

    def extend(self, queue):
        self.elements.extend(queue.elements)

    def next(self):
        if len(self.elements) > 1:
            return Queue(*self.elements[1:])
        else:
            return Queue()

    def __add__(self, other):
        new_queue = Queue(*self.elements)
        new_queue.extend(other)
        return new_queue

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.elements == other.elements

    def __rshift__(self, N):
        return Queue(*self.elements[N:])

    def __str__(self):
        if self.elements:
            return '[' + ' -> '.join(map(str, self.elements)) + ']'
        else:
            return '[]'

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
