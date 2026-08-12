N=[10,5,3,8,15,4]
even=[]
def pushEven(N):
  for i in N:
    if i%2==0:
      even.append(i)
def popEven(even):
  while len(even)!=0:
    print(even.pop(),end=' ')
  else:
    print('stack empty')
pushEven(N)
popEven(even)
