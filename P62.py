class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,r):
        self.r = r
        # super().__init__(r,r)        this will take area method from super class i.e. shape
    
    def area(self):
        return self.r*self.r*(22/7)

rec = Shape(12,24)
print(rec.area())

c = Circle(49)
print(c.area())