import pickle
marks = []
for i in range(5):
    marks.append(int(input("Enter marks: ")))
with open("marks.dat", "wb") as f:
    pickle.dump(marks, f)
with open("marks.dat", "rb") as f:
    data = pickle.load(f)
print("Highest marks =", max(data))