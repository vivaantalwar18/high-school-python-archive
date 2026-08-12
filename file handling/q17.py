import os
eFile="Emp.DAT"
from pickle import load,dump
def writeEmployee(EFile):
  Eobj=open(EFile,'ab+')
  if not Eobj:
    print("File does not create!")
  else:
    print("Enter customer data")
    ch='Y'
    while ch=='Y' or ch=='y':
      ERecord=[]
      ecode=int(input("Enter the code:"))
      ERecord.append(ecode)
      salary=input ("Enter name:").upper()
      ERecord.append(salary)
      dump(ERecord,Eobj)
      ch=input('Add more entry?<y/n>')
      if ch=='y' or ch=='Y':
        continue
      else:
        break
  Eobj.flush()
  Eobj.close()
writeEmployee(eFile)

