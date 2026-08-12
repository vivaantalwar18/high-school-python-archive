def create_file():
    with open("SHIVAJI.TXT", "w") as f:
        f.write("Shivaji was born in the family of Bhonsle.\n")
        f.write("He was devoted to his mother Jijabai.\n")
        f.write("India at that time was under Muslim rule.\n")
def Count_Line():
    myfile = open("SHIVAJI.TXT", "r")
    count = 0
    while True:
        line = myfile.readline()
        if len(line) == 0:
            break
        count += 1
    myfile.close()
    print("Total number of lines:", count)
create_file()
Count_Line()