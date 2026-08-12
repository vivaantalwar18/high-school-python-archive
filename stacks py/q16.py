Courses = [
    ["MCA", 200000, 3],
    ["MBA", 500000, 2],
    ["BA", 100000, 3]
]
Univ = []
def Push_element():
    for course in Courses:
        if course[1] > 100000:
            Univ.append(course)
def Pop_element():
    if len(Univ) == 0:
        print("Underflow")
    else:
        while len(Univ) > 0:
            print(Univ.pop())
Push_element()
Pop_element()