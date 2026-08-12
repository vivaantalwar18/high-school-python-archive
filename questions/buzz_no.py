num = int(input("Enter a number: "))

if num % 10 == 7 or num % 7 == 0:
    print(num, "is a Buzz Number")
else:
    print(num, "is NOT a Buzz Number")