def flat_list(array):
    one_dim_list = []
    for element in array:
        if type(element) == int:
            one_dim_list.append(element)
        else:
            one_dim_list += flat_list(element)
    return one_dim_list
