def flat_list(array):
    one_dimensional_list = []
    for element in array:
        if type(element) == int:
            one_dimensional_list.append(element)
        else:
            one_dimensional_list += flat_list(element)
    return one_dimensional_list
