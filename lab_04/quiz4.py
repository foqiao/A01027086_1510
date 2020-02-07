def statistics(stats_test):
    stats_test = []
    for stats_test in range(len(stats_test) - 1):
        stats_test[0] = stats_test.count()
        stats_test[1] = min(stats_test)
        stats_test[2] = max(stats_test)
        stats_test[3] = int(sum(stats_test)) / int(stats_test.count())
        stats_test[4] = range(min(stats_test), max(stats_test), stats_test.index(0, -1))
    return stats_test

stats_test_input = [1, 23, 56, 2, 5]
statistics(stats_test_input)