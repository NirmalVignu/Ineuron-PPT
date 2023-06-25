class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2

print(stack.is_empty())  # Output: False

print(stack.pop())  # Output: 1

print(stack.is_empty())  # Output: True
