student=[]
ctr=1
while ctr<=40:
  print()
  print('enter data for studenr:%d'%ctr)
  Name = input("Enter name:").upper()
  print("enter 5 subject marks:")
  sub1 = int(input("Enter subject 1 marks:"))
  sub2 = int(input("Enter subject 2 marks:"))
  sub3 = int(input("Enter subject 3 marks:"))
  sub4 = int(input("Enter subject 4 marks:"))
  sub5 = int(input("Enter subject 5 marks:"))
  std=(sub1,sub2,sub3,sub4,sub5)
  student.append(std)
  ctr+=1
print()
print("student list")
print()
print("_"*110)
print()
print("{0:<15}{1:>12}{2:>12}{3:>12}{4:>12}{5:>12}{6:>12}{7:>12}{8:^10}").format("Name","sub1","sub2",)
print("_"*110)