Nums = [213, 10025, 167, 254923, 14, 1297653, 31498, 386, 92765]
BigNums = []
def PushBig():
    for num in Nums:
        if len(str(num)) >= 5:
            BigNums.append(num)
def PopBig():
    if len(BigNums) == 0:
        print("Stack Empty")
    else:
        while len(BigNums) > 0:
            print(BigNums.pop())
        print("Stack Empty")
PushBig()
PopBig()