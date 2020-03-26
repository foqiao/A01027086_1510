class Tree:
    def __init__(self, species, age, trunk_circumference):
        self.species = species
        self.age = age
        self.trunk_circumference = trunk_circumference
        if self.age is None or self.age < 0:
            raise ValueError("Please enter a positive integer before submission")
        if self.trunk_circumference is None or self.trunk_circumference < 0:
            raise ValueError("Please enter a positive integer before submission")
        if self.species is None:
            raise ValueError("Please enter a value before submission")

    def __str__(self):
        print("The tree is called %s. It is %dmm. It is %s wide" % (self.species, self.age, self.trunk_circumference))

    def __repr__(self):
        print("Tree(%s, %d, %d)" % (self.species, self.age, self.trunk_circumference))

def main():
    cedar = Tree(None, 12, 12)
    cedar.__str__()
    cedar.__repr__()

if __name__ == '__main__':
    main()