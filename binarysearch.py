def binarysearch(array, item):
    head = 0
    tail = len(array) -1
    mid = (head + tail) // 2  #for python 3.X floor division
    while (head <= tail):
        if(array[mid] < item):
            head = mid + 1
        elif(array[mid] > item):
            tail = mid - 1
        else:
            return mid
    return None;

