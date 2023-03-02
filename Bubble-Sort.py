def bubble_sort_optimized(Array):
    has_swapped = True
    while(has_swapped):
        has_swapped = False
        for j in range(len(Array) - 1):
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]
                has_swapped = True