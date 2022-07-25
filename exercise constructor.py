class traingle:
    base=""
    height=""
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculate(self,h):
        tri=0.5*self.base*self.height*h
        print(tri)

t=traingle(55,6)
t.calculate(2)
