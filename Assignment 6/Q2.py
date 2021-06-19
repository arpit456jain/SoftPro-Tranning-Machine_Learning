class Rectangle:
    def __init__(self,l,b):
        self.len = l
        self.wid = b

    def rectArea(self):
        Area = self.len * self.wid
        print("Area is ",Area)

    def rectPeri(self):
        Perimeter = 2*(self.len + self.wid)
        print("Perimeter is ",Perimeter)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

obj1 = Rectangle(2,3)
obj1.rectArea()
obj1.rectPeri()
obj2 = Square(2)
obj2.rectArea()
obj2.rectPeri()