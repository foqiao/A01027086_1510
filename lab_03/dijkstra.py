import random


def dijkstra():
    dutch = ["white", "white", "white", "red", "red", "blue", "blue"]
    flag = random.choice(dutch)
    color_arrangement = []
    if flag == dutch[5:6]:
        color_arrangement[0:1] = flag
    elif flag == dutch[0:2]:
        color_arrangement[2:4] = flag
    elif flag == dutch[3:4]:
        color_arrangement[5:6] = flag

    return color_arrangement

dijkstra()