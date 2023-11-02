import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
        print("Created!")

    def area(self):
         return self.radius ** 2 * math.pi
    
circle = Circle(4)
print(circle.area())