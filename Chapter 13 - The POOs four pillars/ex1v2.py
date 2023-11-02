class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    
class Square:
    def __init__(self, s1):
        self.square = s1

    def calculate_parimeter(self):
        return self.square * 4
    
rec = Rectangle(25, 50)
print(rec.calculate_perimeter())

sq = Square(20)
print(sq.calculate_parimeter())