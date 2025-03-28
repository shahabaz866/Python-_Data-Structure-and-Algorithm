def sum_lst(ls):

    if not ls:  
        return 0
    return ls[0] + sum_lst(ls[1:])


print(sum_lst([1,2,3,4,5]))