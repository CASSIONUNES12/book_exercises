class Rider:
    def __init__(self,name):
        self.name = name

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

the_rider = Rider("Juan Caballero")
luna_the_horse = Horse("Luna", the_rider)

print("The name of the horse is {}".format(luna_the_horse.name))
print("The name of the rider is {}".format(luna_the_horse.rider.name))