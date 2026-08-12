n=int(input("enter number "))
data={}
lang=("eng","phy","chem","math")
for i in (0,n):
  name=input('enter name of student %d:'%(i+1))
  marks=[]
  for x in lang:
    marks.append(int(input("enter marks in %s:" %x)))
  data[name]=marks
for x,y in data.items():
  total=sum(y)
  print("%s's total marks %d"%(x,total))
if total < 200:
  print("need improvement")
else:
  print("good performance")