stack=list()
top=-1
def push_element(stack,top):
  ch='y'
  while ch=='y' or ch=='Y' or ch=='yes':
    val=input('ent6er the v€lue ejhvwd')
    stack.append(val)
    top=top+1
    print(',,,')
    ch=input()
    if ch =='n' or ch=='N':
      break
  return top
def Pop_element(stack,top):
  slen=len(stack)
  if slen<=0:
    print("stack is empty")
  else:
    val=stack.pop()
    top=top-1
    print(val)
  return top
def Show_element(stack,top):
  slen=len(stack)
  if slen<=0:
    print("stack is empty")
  else:
    print("")
    i=top
    while  (i>=0):
      print(stack[i])
      i-=1
while True:
  print()
  print("stack op-ert")
  print('-----------')
  print("add")
  print("remove")
  print("SHOW")
  print('exit')
  opt=int(input("enter opinion"))
  print()
  if opt==1:
    top=push_element(stack,top)
  elif opt==2:
    top=pop_element(stack,top)
  elif opt==3:
    show_element(stack,top)
  elif opt==4:
    break

