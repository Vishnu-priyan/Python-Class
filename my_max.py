def maximum(iterable):
    """Returns the maximum of a string if no error else returns -999"""
    max_item = 0
    if type(iterable) == list or type(iterable) == tuple:
        for i in iterable:
            if type(i)==int:
                if max_item<i:
                    max_item = i
            else:
                max_item = -999
                break
    else:

        max_item=-999
    return max_item


a = [12,3,4,5,56]
if maximum(a) != -999:
    print("There is no error")
else:
    print("Error")



