def dijkstra():
    dutch = ["white", "white", "white", "red", "red", "blue", "blue"]
    color_arrangement = []
    for color_order in range(0, 6, 1):
        if dutch[color_order] == "blue":
            color_arrangement[0] = "blue" * 2
        elif dutch[color_order] == "white":
            color_arrangement[2] = "white" * 3
        elif dutch[color_order] == "red":
            color_arrangement[5] = "red" * 2

    return color_arrangement

dijkstra()