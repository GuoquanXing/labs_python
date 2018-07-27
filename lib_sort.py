import random

def quicksort(array):    #random pivot
    if len(array) < 2:
        return array;
    else:
        pivot = array[random.randint(0, len(array)-1)];
        less = [i for i in array[0:] if i < pivot];
        greater = [i for i in array[0:] if i > pivot];
        return quicksort(less) + [pivot] + quicksort(greater)


def bubblesort(array):
    totalLength = len(array)
    for i in range(totalLength):
        for j in range(i + 1, totalLength):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]  # swap two integer
    return array

def quicksortFirstPivot(array):    #always use first index as pivot
    if len(array) < 2:
        return array;
    else:
        pivot = array[0];
        less = [i for i in array[1:] if i < pivot];
        greater = [i for i in array[1:] if i > pivot];
        return quicksort(less) + [pivot] + quicksort(greater)