class Square:

    def __init__(self, s1):
        self.square = s1
        


    def print_size(self):
        return "{} by {} by {} by {}".format(self.square, self.square, self.square, self.square)


square1 = Square(10)
print(square1.print_size())



