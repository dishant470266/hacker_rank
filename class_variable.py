class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def cal_circumfrence(self):
        return 2*Circle.pi*self.radius

c = Circle(5)
c1 = Circle(7)

print(c.cal_circumfrence())