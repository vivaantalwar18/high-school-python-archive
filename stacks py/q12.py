xiia=[]
student=[['Rajveer','9999999999','xi','b'],['Vivaan','8888888888','xii','a'],['Rohan','7777777777','vii','d'],['gabru','6666666666','xii','a']]
def PushElement(student):
  for i in student:
    if i[2]=='xii' and i[3]=='a':
      xiia.append([i[0],i[1]])
def popElement():
  while len(xiia)!=0:
    print(xiia.pop())
  else:
    print('empty stack')
PushElement(student)
print(xiia)
popElement()
