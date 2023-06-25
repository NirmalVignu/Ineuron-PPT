class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")

    def is_empty(self):
        return len(self.queue) == 0
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

print(queue.is_empty())  # Output: False

print(queue.dequeue())  # Output: 3

print(queue.is_empty())  # Output: True
