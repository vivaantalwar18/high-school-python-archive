N=int(input("EnterN-->"))
for i in range(0, N+1, 1):
	if i**2  == N:
		break
	else:
		if i%5 ==0:
			continue
	print (i, end=' ')