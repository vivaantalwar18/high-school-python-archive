cphone=dict()
ch='Y'
print("enter customer details")
while ch=='Y' or ch=="yes":
  print("enter name:",end=" ")
  name=input()
  print("enter phn no:",end=' ')
  phno=input()
  cphone[name]=phno
  print("add more customer <y/n>:",end='')
  ch=input().upper()
  if ch=="N" or ch=="NO":
    break
sname=input("enter name to find phn no.")
flag=0
ckeys=cphone.keys()
for cname in ckeys:
  if cname == sname:
    flag = 1
    break;
if flag==1:
  print(phn no. of %s is %s"%(sname,cphone[cname]))
else:
  print("customer not found")
print()
print("customer list.....")
print("-"*40)
print('{0:<25}{1:>12}'.format('customer name','phn no.'))
print("-"*40)
for cname,phno in cphone.items():
  print('{0:<25}{1:>12}'.format(cname,phno))
print("-"*40)