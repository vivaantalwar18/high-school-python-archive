data=[1,2,3,4,5,6,7,8,9]
stack=[]
def PushElement(stack,data):
  for i in data:
    if i%2==0:
      stack.append(i)
def popElement():
  while len(stack)!=0:
    print(stack.pop())
  else:
    print('stack empty')
PushElement(stack,data)
print(stack)
popElement()