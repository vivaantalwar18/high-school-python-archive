stack=[]
n=int(input("Enter number of elements:"))
def pushElement():
    for i in range(n):
        element=int(input("Enter element:"))
        stack.append(element)
pushElement()
print(stack)