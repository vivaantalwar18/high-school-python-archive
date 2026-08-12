a=int(input("Enter first no.: "))
b=int(input("enter second no: "))
if a>b:
    l=a
else:
    l=b
lcm=l
while True:
    if l%a==0 and l%b==0:
        lcm=l
        break
    l=l+1
print("LCM IS =",lcm)