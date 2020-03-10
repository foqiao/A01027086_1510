import random


def dijkstra():
    dutch = ["red", "white", "blue"]
    dutch_picker = random.choices(dutch, k=7)
    dutch_flag = sorted(dutch_picker, key=lambda dutch_picker: dutch_picker[1])
    print(dutch_flag)

dijkstra()