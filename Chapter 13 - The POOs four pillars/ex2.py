class Square:
    def __init__(self, s1):
        self.square = s1

    def calculate_parimeter(self):
        return self.square * 4
    
    def change_size(self, new_size):
        self.square += new_size

square1 = Square(100)
print(square1.square)

square1.change_size(200)
print(square1.square)

print(square1.calculate_parimeter())