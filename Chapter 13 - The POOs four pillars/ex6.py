class Square:

    square_list = []

    def __init__(self, width, lenght):
        self.width = width
        self.length = lenght
        self.square_list.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


square1 = Square(10, 20)
square2 = Square(20, 30)
square3 = Square(30, 40)
square4 = Square(40, 50)
square5 = Square(50, 60)

print(Square.square_list)

