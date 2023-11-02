class Nationality:
    def __init__(self):
        self.nation = 'nation'

arg = Nationality()
messi = arg
print(messi is arg)

ronaldo = Nationality()
print(ronaldo is arg)