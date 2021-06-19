print("Enter the following Details\n")
name = input("Name  ")
roll = input("Roll  ")
address = input("Address  ")
contactno = input("Contact no  ")

str1 = "Name : "+name + "\nRoll No : "+roll + "\nAddress : "+address  + "\nContat NO" + contactno
f = open("student.txt",'w')
f.write(str1)
f.close()