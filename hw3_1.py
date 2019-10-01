def checkio(list):
    non_uniq = []
    for i in range(len(list)):
        if list[i:].count(list[i]) > 1:
            non_uniq.append(list[i])
    return non_uniq
