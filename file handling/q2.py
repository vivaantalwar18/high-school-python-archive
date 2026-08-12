import os
notes_dict = {
    1: "India is the fastest growing economy.",
    2: "Kids are the future of the nation.",
    3: "Kindness is a great virtue.",
    4: "The whole world is looking at India as a great market.",
    5: "Keep working hard!"
}
def createFile():
    with open("MYNOTES.TXT", "w") as f:
        for key in notes_dict:
            f.write(notes_dict[key] + "\n")
    print("MYNOTES.TXT created successfully\n")
def LinesWithK():
    if os.path.isfile("MYNOTES.TXT"):
        fb = open("MYNOTES.TXT", "r")
        print("The lines are ...")
        while True:
            line = fb.readline()
            line = line.rstrip()
            if not line:
                break
            if line[0].upper() == 'K':
                print(line)
        fb.close()
    else:
        print("Source file does not exist!")
createFile()
LinesWithK()