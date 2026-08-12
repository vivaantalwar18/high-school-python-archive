import pickle
a=open("journal.txt","w")
j=[]
while True:
    dob=input("Enter date in format [YYYY-MM-DD]:")
    mood=input("Enter mood (happy/sad/neutral):")
    note=input("Enter a note:")
    a.write(dob)
    a.write('\t')
    a.write(mood)
    a.write('\t')
    a.write(note)
    a.write('\n')
    ch=int(input("Enter 1 to continue and 0 to break:"))
    if ch==1:
        continue
    elif ch==0:
        break
    else:
        print("Incorrect value. Please try again!")
a.close()
b=open("journal.txt","r")
i=0
while True:
    c=b.readline()
    print(c)
    if not c:
        break
    i=i+1
print("Count:",i)
b.close()