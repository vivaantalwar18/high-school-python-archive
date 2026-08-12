x=int(input("Enter the first no.:  "))
y=int(input("Enter second no.:  "))
if x>y:
	smaller=y
else:
	smaller=x
i=1
while (i<=smaller):
	if((x%i==0) and (y%i==0)):
		HCF=i
	i=i+1
print("HCF = ",HCF)