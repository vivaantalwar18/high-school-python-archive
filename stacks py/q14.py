data=[['pen',120.00,'pcs','Reynolds',132.00],['paper',345.00,'rims','Camel',500.00],['eraser',100.00,'box','IBP',110.00]]
stack=[]
def PushElement(stack,data):
  for i in data:
    if i[1]==i[4]*0.90:
      stack.append(i)
def print_stack():
  cnt=len(stack)
  while stack !=[]:
    item=stack.pop()
    print(item[0])
  else:
    print('total items in stack',cnt)
PushElement(stack,data)

print_stack()

