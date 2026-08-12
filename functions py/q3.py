# Developing a power function using default parameter
def power(n, p=2):
    s = 1
    for i in range(1, p+1):
        s = s * n
    return s
def main():
    num = int(input("Enter the number: "))
    p = int(input("Enter the power to be calculated: "))
    result = power(num, p)
    print("Result when the power is given:", result)
    result = power(num)
    print("Result when the power is not given (default 2):", result)
main()