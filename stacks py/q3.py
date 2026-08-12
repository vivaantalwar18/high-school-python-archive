stack = []
n = int(input("Enter number of numbers to push into stack: "))
for i in range(n):
    num = int(input("Enter number: "))
    stack.append(num)
print("Stack:", stack)
if len(stack) >= 2:
    a = stack.pop()
    b = stack.pop()
    add = a + b
    print(f"{b} + {a} = {add}")
    sub = b - a
    print(f"{b} - {a} = {sub}")
    mul = a * b
    print(f"{b} * {a} = {mul}")
    if a != 0:
        div = b / a
        print(f"{b} / {a} = {div}")
    else:
        print("Cannot divide by zero!")
else:
    print("Need at least 2 numbers in stack for operations.")