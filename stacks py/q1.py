MAX = 3
stack = []
for i in range(4):
    if len(stack) >= MAX:
        print("Stack Overflow! Cannot push", i+1)
    else:
        stack.append(i+1)
        print(i+1, "pushed")
for i in range(4):
    if not stack:
        print("Stack Underflow! Cannot pop")
    else:
        print(stack.pop(), "popped")