def computeavg(list1,n):
  t=0
  for marks in list1:
    t=t+marks
  avg=t/n
  return avg
list1=[]
print("How many students marks u want to enter: ")
n=int(input())
for i in range(0,n):
  print("enter marks of students",(i+1),":")
  marks = int(input())
  list1.append(marks)
avg=computeavg(list1,n)
print("avg marks of",n,"students is:",avg)