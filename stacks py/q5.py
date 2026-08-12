months=[]
n=int(input("Enter number of months:"))
for i in range(1,n+1):
    month=input("Enter month:")
    months.append(month)
print(months)
def popElement():
    if not months:
        print("Stack is empty")
    else:
        n=months.pop()
        print("Element popped from stack")
popElement()
print(months)