stack = []
T = -1
def pushElement():
    global T
    while True:
        element = input("Enter element (or 'q' to quit): ")
        if element.lower() == 'q':
            break
        try:
            num = int(element)
            stack.append(num)
            T += 1
            print("Element pushed into stack")
        except ValueError:
            print("Invalid input! Enter an integer.")
    print("Final stack:", stack)
pushElement()