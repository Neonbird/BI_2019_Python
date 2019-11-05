def create_intervals(data):
    list_of_int = sorted(data)
    intervals = []
    for i in range(len(list_of_int)):
        if i == 0 or list_of_int[i] != list_of_int[i - 1] + 1:
            intervals.append([list_of_int[i]])
        if i == len(list_of_int) - 1 or list_of_int[i] != list_of_int[i + 1] - 1:
            intervals[-1].append(list_of_int[i])
    intervals = list(map(tuple, intervals))
    return intervals


print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])
print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)])
