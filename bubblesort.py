def bubblesort(array):
    n = 0
    while n < len(array) - 1:
        if array[n] > array[n + 1]:
            n1 = array[n]
            n2 = array[n + 1]
            array[n] = n2
            array[n + 1] = n1
            n = 0
        else:
            n = n + 1

numbers = [7, 48, 5, 104, 107]
bubblesort(numbers)
print(numbers)