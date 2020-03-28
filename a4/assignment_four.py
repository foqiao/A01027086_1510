class TreeFarm:
    def __init__(self, tree_name, Type, age, trunk_circumference):
        self.tree_name = tree_name
        self.Type = Type
        self.trunk_circumference = trunk_circumference
        self.age = age

    def add(self):
        tree_database = ["fir", "deciduous"]
        tree_list = {}
        for i in tree_database:
            if self.Type == i:
                tree_list.update({"tree-spec": [self.tree_name, self.Type, self.age, self.trunk_circumference]})
            else:
                pass

    def remove_tree(self, trunk_circumference):
        for self.trunk_circumference in tree_list:
            if trunk_circumference <= self.trunk_circumference:
                print("Harvest %s" % trunk_circumference)
                del self.trunk_circumference
                break

    def remove_trees(self, trunk_circumference):
        for self.trunk_circumference in tree_list:
            if trunk_circumference <= self.trunk_circumference:
                print("Harvest %s" % trunk_circumference)
                del trunk_circumference