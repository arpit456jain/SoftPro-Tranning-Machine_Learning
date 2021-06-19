class Interset:
    def __init__(self,p,n,r):
        self.p = p
        self.n = n
        self.r = r

    def simpleInterset(self):
        SI = (self.p * self.n * self.r)/100
        print("Simple Interset is ",SI)
if __name__ == "__main__":
    si1 = Interset(10,20,2)
    si1.simpleInterset()
