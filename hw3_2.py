def flat_list(array):
    one_dem_l = []
    for i in array:
        if type(i) == int:
            one_dem_l.append(i)
        else:
            one_dem_l += flat_list(i)
    return(one_dem_l)