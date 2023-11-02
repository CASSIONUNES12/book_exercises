class Shape:
    def what_am_i(self):
        print("I am a Shape")
        

class Square(Shape):
    sqr_list = []

    def __init__(self, s1):
        self.square = s1
        self.sqr_list.append(self)

    def calculate_perimeter(self):
        return self.square * 4
    
    def what_am_i(self):
        return super().what_am_i()
    print("I am a Square")
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.square, self.square, self.square, self.square)
    
square1 = Square(29)
print(square1)
