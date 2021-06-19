class Parent:
    def funcl(self):
        print("this is function one")


class Child(Parent):
    def func2(self):
        print("this is function two")


y = Child()
y.funcl()
y.func2()