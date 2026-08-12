stack = []
exp = input("Enter a postfix expression (e.g. 23+5*): ")
for ch in exp:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)
print("Result of expression:", stack.pop())