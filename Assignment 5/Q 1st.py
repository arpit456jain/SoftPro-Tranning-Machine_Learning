class Student:
    def setValue(self,rollno,name ,fee):
        self.rollno = rollno
        self.name = name
        self.fee = fee

    def display(self):
        print("Roll No is ",self.rollno,"\nName is ",self.name,"\nFee is ",self.fee)

if __name__ == "__main__":
    student1 = Student()
    student1.setValue(1,"Arpit",1000)
    student1.display()
