from collections import deque

stack = deque()

# Push elements onto stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements (Last-In-First-Out)
print("Stack:")
while stack:
    print(stack.pop())
