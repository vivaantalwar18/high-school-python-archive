print("The prime no. are",end=" ")
for i in range(1,20):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i,end=" ")