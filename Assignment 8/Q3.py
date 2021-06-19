str1 = "A car is a vehicle that has wheels, carries a small number of passengers, and is moved by an engine or a motor. Cars are also called automobiles or motor vehicles. Trucks and buses are motor vehicles as well. However, trucks and buses are larger than cars, and they carry heavier loads."
import re
word = "a"
c=0
str1 = re.sub("[^\w]", " ",  str1).split()
print(str1)
for i in str1:
    if i == word:
        c=c+1
    else:
        pass

print(word,"occurs in text given is ", c)