class Horse:
    def __init__(self, name, color, owner):
        self.name = name
        self.color = color
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

rider1 = Rider("Juan Caballero")

horse1 = Horse("Atena", "brown", rider1)
print(horse1.owner.name)