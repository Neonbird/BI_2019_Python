def flat_list(array):
    one_dimensional_list = []
    for element in array:
        if type(element) is list:
            one_dimensional_list += flat_list(element)
        else:
            one_dimensional_list.append(element)
    return one_dimensional_list
