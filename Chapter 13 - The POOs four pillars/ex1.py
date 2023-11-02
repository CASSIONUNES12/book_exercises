class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Rectangle(Shape):
        pass
            

class Square(Shape):
        pass
       


rec = Rectangle(50, 25)
print(rec.calculate_perimeter())

sq = Square(20, 20)
print(sq.calculate_perimeter())
        
        
    
