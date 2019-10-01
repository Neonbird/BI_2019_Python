def checkio(list):
    non_uniq = []
    for elem in list:
        if list.count(elem) > 1:
            non_uniq.append(elem)
    return non_uniq
