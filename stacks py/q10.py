stack=[]
MAX=5
def PushElement(element):
  if len(stack)==MAX:
    print("stack overflow!cannot push",element)
  else:
    stack.append(element)
    print(f"Element {element} pushed into stack.")
def popElement():
  if not stack:
    print("stack underflow! No element to pop")
  else:
    ele=stack.pop()
    print(f"Element {ele} popped from stack.")
def peek():
  if not stack:
    print("stack is empty,nothing to peek")
  else:
    print("Top element is:  ",stack[-1])
def display():
  if not stack:
    print("stack is empty i.e underflow")
  else:
    print("stack elements are (top to bottom): ")
    for i in range (len(stack)):
      print(stack[i])
def main():
  while True:
    print("\n---stack menu---")
    print("1.push element")
    print("2.pop element")
    print("3.peek element")
    print("4.display stack")
    print("5.exit")
    ch=int(input("enter choice: "))
    if ch==1:
      element=int(input("enter element to push "))
      PushElement(element)
    elif ch==2:
      popElement()
    elif ch==3:
      peek()
    elif ch==4:
      display()
    elif ch==5:
      print("exiting program")
      break
    else:
      print("invalid choice! pl try again")
main()