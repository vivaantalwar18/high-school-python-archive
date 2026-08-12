N=['ANKITA', 'NITISH', 'ANWAR', 'DIMPLE', 'HARKIRAT']
onlyA=[]
def PUSH(N):
  for i in N:
    if 'A' in i:
      onlyA.append(i)
def popA(onlyA):
  if len(onlyA)==0:
    print("stack empty")
  else:
    while len(onlyA)>0:
      print(onlyA.pop(),end=' ')
    print("empty")
PUSH(N)
popA(onlyA)