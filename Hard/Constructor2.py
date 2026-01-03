#area and parameter
class rectangle:
        def __init__(self,length,breadth):
                self.length = length
                self.breadth = breadth
        def area(self):
                area = self.length*self.breadth
                return area
        def perimeter(self):
                perimeter = 2 *(self.length + self.breadth)
                return perimeter
        def display(self):
                print("rectangle with",self.length,"and",self.breadth,"has area",self.area(),"and perimeter",self.perimeter())

rect1=rectangle(5,10)
rect2=rectangle(7,3)

rect1.display()
rect2.display()

