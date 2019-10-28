def create_intervals(data):
    list_of_int = sorted(list(data))
    intervals = []
    j = -1
    for i in range(len(list_of_int)):
        if i == 0 or list_of_int[i] != list_of_int[i - 1] + 1:
            intervals.append([list_of_int[i]])
            j += 1
        if i == len(list_of_int) - 1 or list_of_int[i] != list_of_int[i + 1] - 1:
            intervals[j].append(list_of_int[i])
    intervals = [tuple(interval) for interval in intervals]
    return intervals

print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])