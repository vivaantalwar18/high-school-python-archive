import os
def create_file():
    with open("MAGIC.TXT", "w") as f:
        f.write("The magic of 5 young friends can be compared with 3 children.\n")
        f.write("The young ones are in age 18 and the children are below 10.")
    print("MAGIC.TXT file created successfully with content!\n")
def count_file():
    txtfile = "MAGIC.TXT"
    if os.path.isfile(txtfile):
        with open(txtfile, "r") as fb:
            alphabets = digits = spaces = lines = 0
            print("File contents are:\n")
            while True:
                line = fb.readline()
                if not line:
                    break
                print(line, end="")
                lines += 1
                for ch in line:
                    if ch.isalpha():
                        alphabets += 1
                    elif ch.isdigit():
                        digits += 1
                    elif ch.isspace():
                        spaces += 1
        print("\n")
        print("Total lines:", lines)
        print("Total alphabets are:", alphabets)
        print("Total digits are:", digits)
        print("Total spaces are:", spaces)
    else:
        print("File does not exist!")
create_file()
count_file()