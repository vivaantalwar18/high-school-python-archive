a=open("data.txt","w")
a.write("India is great")
a.write("\n")
a.write("We are great")
a.close()
b=open("data.txt","r")
d1=b.read(5)
for i in d1:
    if i in "AEIOUaeiou":
        print(i, "is a vowel")
    else:
        print(i, end=" ")
b.close()