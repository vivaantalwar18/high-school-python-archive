a=[55,2,33,64,11,123,32,56]
l=len(a)
for i in range(0,l):
	for j in range(0,l-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print(a)