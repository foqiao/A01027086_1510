def dijkstra():
    dutch = ["white", "white", "white", "red", "red", "blue", "blue"]
    color_arrangement = {}
    for color_order in range(0, 7, 1):
        if dutch[color_order] == "blue":
            color_arrangement.append("blue" * 2)
        elif dutch[color_order] == "white":
            color_arrangement.append("white" * 3)
        elif dutch[color_order] == "red":
            color_arrangement.append("red" * 2)
    return color_arrangement

if __name__ == '__main__':
    dijkstra()