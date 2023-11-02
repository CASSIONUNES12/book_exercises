import math

class Triangle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calculate_area(self):
        return self.base * self.altura / 2
    
triangulo = Triangle(20, 30)
print(triangulo.calculate_area())