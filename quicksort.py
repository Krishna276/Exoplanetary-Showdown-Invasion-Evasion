def quicksort(lst: list) -> list:
    '''A fast recursive sorting algorithm.'''
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    left: list = []
    right: list = []

    for item in lst[:-1]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    
    return quicksort(left) + [pivot] + quicksort(right)
