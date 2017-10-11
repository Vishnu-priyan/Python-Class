def pop(my_list):
    """delet last element and print"""
    temp = my_list[-1]
    del my_list[-1]
    return temp



def count(my_list,myvar):
    count = 0
    for item in my_list:
        if item==myvar:
            count+=1
    return count



