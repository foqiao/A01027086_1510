import random


def dijkstra():
    dutch_flag = []
    dutch = ["red", "white", "blue"]
    dutch_picker = random.choices(dutch, k=7)
    for i in dutch_picker:
        if i == "red":
            dutch_flag.insert(0, i)
        if i == "white":
            dutch_flag.insert(2, i)
        if i == "blue":
            dutch_flag.insert(6, i)
    print(dutch_flag)

dijkstra()