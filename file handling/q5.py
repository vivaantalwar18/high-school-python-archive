import os
def CreateIndiaFile():
    f = open("INDIA.TXT", "w")
    text = input("Enter text for INDIA.TXT file:\n")
    f.write(text)
    f.close()
    print("File created successfully.\n")
def WordIndia():
    CountWord = 0
    if os.path.isfile('INDIA.TXT'):
        fobj = open('INDIA.TXT', 'r')
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
CreateIndiaFile()
WordIndia()