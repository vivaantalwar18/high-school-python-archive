import csv
f = open("results.csv", "w", newline='')
writer = csv.writer(f)
examdata = [["Name", "Marks", "Rank"],
            ["Sheela", 450, 1],
            ["Rohan", 300, 2],
            ["Akash", 260, 3]]
writer.writerows(examdata)
f.close()
with open("results.csv", "r") as NF:
    NewReader = csv.reader(NF)
    for rec in NewReader:
        print(rec[0], rec[1], rec[2])