def statistics(stats_test):
    stats_test = [1, 23, 56, 2, 5, 6]
    stats_test_result = []
    stats_test_result[0] = stats_test.count()
    stats_test_result[1] = min(stats_test)
    stats_test_result[2] = max(stats_test)
    stats_test_result[3] = int(sum(stats_test)) / int(stats_test.count())
    stats_test_average = max(stats_test) - min(stats_test)
    stats_test_result[4] = range(min(stats_test), max(stats_test), stats_test.index(0, -1) + 1)
    return stats_test_result

if __name__ == '__main__':
    statistics(stats_test=True)