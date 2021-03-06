from a4.assignment_four import TreeFarm

def main():
    name = str(input("Please enter the name of the wood you want to store: "))
    Type = str(input("Please enter the Type of the wood you want to store: "))
    circumference = int(input("Please enter the circumference of the lumber: "))
    age = int(input("Please enter the age of the wood you input: "))
    lumber = TreeFarm(name, Type, circumference, age)
    LumberCompany(lumber)


def LumberCompany(lumber):
    """
    front end input for lumber specs from the user
    :param lumber: lumber stored in TreeFarm class
    :return: choose from the dictionary by keys. After punch the key in, the matching service will be in place
    """
    print("lumber_menu = {"
          " 1: Add tree, "
          " 2: Harvest a tree, "
          " 3: Harvest some trees, "
          " 4: quit "
          "}")

    lumber_menu_choice = int(input("Please enter an integer from 1 to 4:"))
    if lumber_menu_choice == 1:
        main()
    if lumber_menu_choice == 2:
        circumference_input = int(input("Please enter the circumference of the wood you want to harvest: "))
        lumber.remove_tree(circumference_input, tree_list=lumber)
        LumberCompany(lumber)
    if lumber_menu_choice == 3:
        circumferences_input = int(input("Please enter the circumference of the woods you want to harvest " +
                                         "together: "))
        lumber.remove_trees(circumferences_input,  tree_list=lumber)
        LumberCompany(lumber)
    if lumber_menu_choice == 4:
        quit()

if __name__ == '__main__':
    main()