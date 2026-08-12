a=open("data.fl","w")
a.write("abcd\nefg\nhijk\nlmnop\nqrstuv\nwxyz")
a.close()
b=open("data.fl","r")
c=1
while True:
    ln=b.readline()
    if not ln:
        break
    print(c,ln,end="")
    c=c+1
b.close()