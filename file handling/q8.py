import pickle
def WriteRec():
    fobj = open("PATIENTS.dat", "ab")
    try:
        n = int(input("How many records to add? : "))
        for i in range(n):
            print("\nEnter patient details:")
            pid = int(input("Patient ID: "))
            name = input("Name: ")
            disease = input("Disease: ")
            rec = [pid, name, disease]
            pickle.dump(rec, fobj)
    except Exception as e:
        print("Error:", e)
    finally:
        fobj.close()
def countrec():
    fobj = open("PATIENTS.dat", "rb")
    count = 0
    try:
        while True:
            rec = pickle.load(fobj)
            if rec[2] == "COVID-19":
                print(rec)
                count += 1
    except EOFError:
        pass
    finally:
        fobj.close()
    print("\nTotal number of COVID-19 patients:", count)
WriteRec()
countrec()