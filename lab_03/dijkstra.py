import random


def dijkstra(flag_to_be_sorted):
    #dutch_flag = []
    # dutch = ["red", "white", "blue"]
    # dutch_picker = random.choices(dutch, k=7)
    for i in dutch_picker:
        if i == "red":
            dutch_flag.insert(0, i)
        if i == "white":
            dutch_flag.insert(2, i)
        if i == "blue":
            dutch_flag.insert(6, i)
    print(dutch_flag)


def main():
    flag = ["red", "white", "red", "blue", "blue", "white", "white"]
    dijkstra(flag)