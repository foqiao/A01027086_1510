def dijkstra(flag: list):
    sorted_flag = sorted(flag, key=lambda x: x[1])
    return sorted_flag

def main():
    flag = ["red", "white", "red", "blue", "blue", "white", "white"]
    print(dijkstra(flag))

if __name__ == '__main__':
    main()