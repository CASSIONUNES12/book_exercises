class Apple:
    def __init__(self, c, s, f, w):
        self.color = c
        self.size = s
        self.form = f
        self.weight = w
        print("Created!")

maçã = Apple("green", 8, "round", 200)
print(maçã.color)
print(maçã.size)
print(maçã.form)
print(maçã.weight)