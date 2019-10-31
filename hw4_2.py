def group_equal(ungrouped):
    grouped_list = []
    for i in range(len(ungrouped)):
        if i == 0 or ungrouped[i] != ungrouped[i - 1]:
            grouped_list.append([ungrouped[i]])
        else:
            grouped_list[-1].append(ungrouped[i])
    return grouped_list


print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]])
print(group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]])
print(group_equal([1]) == [[1]])
print(group_equal([]) == [])
