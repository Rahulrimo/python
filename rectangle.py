class Rectangle:
    def __init__(self, height, width):
        print(f"A rectangle is created  with height: {height} and width: {width}")
        self.height = height
        self.width = width
        
        
    def set_dimensions(self, height, width):
        self.height =  height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
rectangle1 = Rectangle(4,3)
rectangle2 = Rectangle(5,6)
rectangle3 = Rectangle(2,8)
# rectangle1.set_dimensions(4,3)
# print("height and width:", rectangle1.height, rectangle1.width)
# print("Area:", rectangle1.area())
# print("Perimeter:", rectangle1.perimeter())