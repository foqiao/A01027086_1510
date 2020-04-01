def dijkstra(flag: list):
    alpha_order = []
    for i in flag:
        alpha_order.append(i[1])
        alpha_order.sort()
    flag.sort(key=lambda alpha: alpha_order)
    return flag

def main():
    flag = ["red", "white", "red", "blue", "blue", "white", "white"]
    print(dijkstra(flag))

if __name__ == '__main__':
    main()