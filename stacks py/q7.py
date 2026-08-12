stack=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    element=int(input("Enter element:"))
    stack.append(element)
print("Stack elements are:")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])