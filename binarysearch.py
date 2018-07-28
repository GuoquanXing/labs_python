def binarysearch(array, item):
    head = 0
    tail = len(array) -1

    while (head <= tail):
        mid = (head + tail) // 2  # for python 3.X floor division
        if(array[mid] < item):
            head = mid + 1
        elif(array[mid] > item):
            tail = mid - 1
        else:
            return mid
    return None;


array = [1,2,3,4,5,6,7,8,9]

print(binarysearch(array, 6))    # expected output is 5

