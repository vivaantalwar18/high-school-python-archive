emp={}
def employeedict(emp):
  ch='Y'
  while ch=='Y' or ch=="yes":
    print("enter name:",end=" ")
    name=input()
    print("enter phn no:",end=' ')
    phno=input()
    emp[name]=phno
    print(  "add more employee <y/n>:",end='')
    ch=input().upper()
    if ch=="N" or ch=="NO":
      break
employeedict(emp)
ekey=list(ekey)
elist.sort()
print()
print("employee list.....")
print("-"*40)
print('{0:<25}{1:>12}'.format('employee name','phn no.'))
print("-"*40)
for i in elist:
  print('{0:<25}{1:>12}'.format(i,emp[i]))
print("-"*40)