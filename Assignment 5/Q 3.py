class Rectangle():
    def __init__(self,len,wid):
        self.len = len
        self.wid = wid

    def rectArea(self):
        Area = self.len * self.wid
        print("Area of Rectangle is ",Area)

    def rectPeri(self):
        Perimeter = 2*(self.len + self.wid)
        print("Perimeter of Rectangle is ",Perimeter)

if __name__ == '__main__':
    r1  = Rectangle(2,3)
    r1.rectArea()
    r1.rectPeri()

