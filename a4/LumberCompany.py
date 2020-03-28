from a4.assignment_four import TreeFarm


def LumberCompany():

    lumber_name = str(input("Please enter the name of the wood you want to store: "))
    lumber_Type = str(input("Please enter the Type of the wood you want to store: "))
    lumber_circumference = int(input("Please enter the circumference of the lumber: "))
    lumber_age = int(input("Please enter the age of the wood you input: "))
    lumber = TreeFarm(lumber_name, lumber_Type, lumber_circumference, lumber_age)

    print("lumber_menu = {"
          " 1: Add tree, "
          " 2: Harvest a tree, "
          " 3: Harvest some trees, "
          " 4: quit "
          "}")

    lumber_menu_choice = int(input("Please enter an integer from 1 to 4:"))
    while 1 <= lumber_menu_choice <= 4:
        if lumber_menu_choice == 1:
            TreeFarm.add(lumber)
            pass
        if lumber_menu_choice == 2:
            circumference_input = int(input("Please enter the circumference of the wood you want to harvest: "))
            TreeFarm.remove_tree(circumference_input)
        if lumber_menu_choice == 3:
            circumferences_input = int(input("Please enter the circumference of the woods you want to harvest " +
                                             "together: "))
            TreeFarm.remove_trees(circumferences_input)
        if lumber_menu_choice == 4:
            break

if __name__ == '__main__':
    LumberCompany()