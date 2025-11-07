class rectangle:
    def getData(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle",self.length*self.breadth)
    def perimeter(self):
        print("perimeter of rectangle",2*self.length+self.breadth)


l=float(input("Enter the length:"))
b=float(input("Enter the breadth:"))
obj=rectangle()
obj.getData(l,b)
obj.area()
obj.perimeter()        
        
