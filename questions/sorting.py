a=[7,11,18,3,31,10,8]
l=len(a)
for i in range(1,l):
	value=a[i]
	pos=i
	while pos>0 and value<a[pos-1]:
		a[pos]=a[pos-1]
		pos=pos-1
		a[pos]=value
print(a)