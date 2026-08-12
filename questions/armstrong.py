#armstrong
n=int(input("Enter a number: "))
num=n
b=[]
q=str(n)
a=list(q)
l=len(a)
for i in range(l):
    n1=n%10
    n=n//10
    b.append(n1)
print(b)
s=0
for i in b:
    s=s+(i**3)
print("sum is=>",s)
if s==num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")