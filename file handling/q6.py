import os
def CreateFile():
    f = open("INDIA.TXT", "w")
    print("Enter text for the file (type END to stop):")
    while True:
        line = input()
        if line == "END":
            break
        f.write(line + "\n")
    f.close()
    print("File created successfully.\n")
def WordIndia():
    CountWord = 0
    if os.path.isfile("INDIA.TXT"):
        fobj = open("INDIA.TXT", "r")
        lines = fobj.read()
        while lines:
            words = lines.split()
            for w in words:
                if w == "India":
                    CountWord = CountWord + 1
            lines = fobj.read()
        print("Total number of words:", CountWord)
        fobj.close()
    else:
        print("File does not exist.")
CreateFile()
WordIndia()