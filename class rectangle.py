class Rectangle:
    def getValues(self,length,breadth):
        self.len=length
        self.breadth=breadth
    def area(self):
        return(self.len*self.breadth)
    def perimeter(self):
        return 2*(self.len+self.breadth)
l=int(input("enter the length"))
b=int(input("enter the breadth"))
rect=Rectangle()
rect.getValues(l,b)
print("Area of rectangle:",rect.area())
print("Area of perimeter:",rect.perimeter())
