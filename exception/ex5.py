f=None
try:
    f = open("exception/student.txt","r")

    print(f.readlines())
except FileNotFoundError as fe:
    print(fe)
finally:
    if(f):
        f.close()
        print("File close successfully")
    else:
        print("File not found so no closing")

    