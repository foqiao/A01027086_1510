import random

def dijkstra(dutch):
    color = random.choice(dutch)
    random_color = int(len(str(color)))
    for random_color in range(0, 5):
        if int(random_color) == 3:
            print(color)
        elif int(random_color) == 4:
            print(color)
        elif int(random_color) == 5:
            print(color)
        else:
            return None