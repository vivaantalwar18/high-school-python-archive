def menuprog():
    def plus():
        x=int(input("Enter the value of x:"))
        y=int(input("Enter the value of y:"))
        s=x+y
        print("Sum of x and y is:",s)
    def prod():
        x=int(input("Enter the value of x:"))
        y=int(input("Enter the value of y:"))
        p=x*y
        print("Product of x and y is:",p)
    ch=int(input("Enter 1 for addition and 2 for product"))
    if ch==1:
        plus()
    elif ch==2:
        prod()
    else:
        print("Invalid choice")
menuprog()