from numpy import NaN

class TreeFarm:
    def __init__(self, tree_name, Type, age, trunk_circumference):
        """
        store the specs of input trees
        :param tree_name: what is the tree's name
        :param Type: what kind of species does the tree belongs to
        :param age: how old of the tree since it planted
        :param trunk_circumference: how to wide is the tree
        """
        self.tree_name = tree_name
        self.Type = Type
        self.trunk_circumference = trunk_circumference
        self.age = age

    def add(self, Type):
        """
        add trees that fits the type in the database
        :param Type: the tree types available in the database
        :return: add tree if input matched or else reject the input request
        """
        tree_database = ["fir", "deciduous"]
        tree_list = []
        for i in tree_database:
            if Type == i:
                tree_list.append(self.tree_name)

    def remove_tree(self, trunk_circumference):
        """
        remove a single tree from the storage
        :param trunk_circumference: identify the minimum size of the tree you want to harvest
        :return: tell user the matched tree is harvested and remove it from the tree_list
        """
        if trunk_circumference <= self.trunk_circumference:
            print("Harvest %s" % self.tree_name)
            del self.tree_name, self.Type, self.trunk_circumference, self.age
            try:
                trunk_circumference = NaN
            except ValueError:
                print("Try a numeric value")

    def remove_trees(self, trunk_circumference):
        """
        remove a bunch of trees from the list
        :param trunk_circumference: identify the minimum size of the trees you want to harvest
        :return: tell user the matched tree is harvest and remove it
        """
        for lumber.trunk_circumference in tree_list:
            if trunk_circumference <= self.trunk_circumference:
                print("Harvest %s" % self.tree_name)
                del self.tree_name, self.Type, self.trunk_circumference, self.age
                try:
                    trunk_circumference = NaN
                except ValueError:
                    print("Try a numeric value")