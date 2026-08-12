a=[]
for i in range(1,20):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		a.append(i)
print(a)
for p in a:
	for q in a:
		if p+q in a:
			print(p,q)
		else:
			continue