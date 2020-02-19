import random


def dijkstra():
    dutch = ["white", "white", "white", "red", "red", "blue", "blue"]
    color_arrangement = ""
    if dutch[5:6] == random.choice(dutch):
        color_arrangement.append(random.choice(dutch))
    elif dutch[0:2] == random.choice(dutch):
        color_arrangement.append(random.choice(dutch))
    elif dutch[3:4] == random.choice(dutch):
        color_arrangement.append(random.choice(dutch))

    return color_arrangement

dijkstra()