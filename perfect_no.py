a = int(input("enter no to check"))
limit = a//2
sum = 0
for i in range(1,limit+1,1):
	if(a%i == 0):
		sum = sum + i
	else:
		continue
if sum==a:
	print("Perfect Number")
else:
	print("Not Perfect Number")