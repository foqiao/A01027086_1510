class Tree:
    def __init__(self, species, age, trunk_circumference):
        """
        store tree specification
        :param species: what kind of tree to store
        :param age: how old is the tree
        :param trunk_circumference: how big is the tree
        """
        self.species = species
        self.age = age
        self.trunk_circumference = trunk_circumference
        if self.age < 0:
            raise ValueError("Please enter a positive integer before submission")
        if self.trunk_circumference < 0:
            raise ValueError("Please enter a positive integer before submission")
        if self.species is None:
            raise ValueError("Please enter a value before submission")

    def __str__(self):
        """
        :return: a string contains some specs of the input tree
        """
        print("The tree is called %s. It is %dmm. It is %s wide" % (self.species, self.age, self.trunk_circumference))

    def __repr__(self):
        """
        :return: a string represent format stored inside the __init__
        """
        print("Tree(%s, %d, %d)" % (self.species, self.age, self.trunk_circumference))