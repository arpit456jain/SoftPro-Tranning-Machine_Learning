f = open("student.txt",'r')
if f.mode == "r":
    content = f.read()
    print(content)

f.close()