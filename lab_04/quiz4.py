def statistics(list_of_integers):
    statistics_list = []
    statistics_list.append(len(list_of_integers) )
    statistics_list.append(min(list_of_integers) )
    statistics_list.append(max(list_of_integers) )
    statistics_list.append(int(sum(list_of_integers)) / len(list_of_integers) )
    statistics_list.append(max(list_of_integers) - min(list_of_integers))
    return statistics_list


def main():
    stats_test_input = [1, 23, 56, 2, 5]
    special_list = statistics(stats_test_input)
    print(special_list)


if __name__ == "__main__":
    main()


