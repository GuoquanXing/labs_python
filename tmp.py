from .lib_sort import quicksort, bubblesort,quicksortFirstPivot
from .binarysearch import binarysearch
from .timeUtil import getCurrentTime, calculateTimeDiff
import random


def calculateElapsedTimeQuicksort(array):
    timestamp_start = getCurrentTime()
    print("timestamp before sorting: %s" + str(timestamp_start))
    sortList = quicksort(array)
    timestamp_stop = getCurrentTime();
    print("timestamp after sorting: %s" + str(timestamp_start))
    print("total elapsed time using quicksort: %s" + str(calculateTimeDiff(timestamp_start, timestamp_stop)))

def calculateElapsedTimeQuicksortFirstPivot(array):
    timestamp_start = getCurrentTime()
    print("timestamp before sorting: %s" + str(timestamp_start))
    sortList = quicksortFirstPivot(array)
    timestamp_stop = getCurrentTime();
    print("timestamp after sorting: %s" + str(timestamp_start))
    print("total elapsed time using quicksortFirstPivot: %s" + str(calculateTimeDiff(timestamp_start, timestamp_stop)))

def calculateElapsedTimeBubblesort(array):
    timestamp_start = getCurrentTime()
    print("timestamp before sorting: %s" + str(timestamp_start))
    sortList = bubblesort(array)
    timestamp_stop = getCurrentTime();
    print("timestamp after sorting: %s" + str(timestamp_start))
    print("total elapsed time using bubblesort: %s" + str(calculateTimeDiff(timestamp_start, timestamp_stop)))

unsortedList = [3, 2, 6, 1, 4, 3, 4, 324, 34523, 23423, 23423, 234, 234, 23423, 234, 234, 2342, 3423, 4423, 42434, 234,
                2342]
unsortedList1 = []
for i in range(100):
    unsortedList1 += [random.random()]

calculateElapsedTimeBubblesort(unsortedList1)
print()
calculateElapsedTimeQuicksortFirstPivot(unsortedList1)
print()
calculateElapsedTimeQuicksort(unsortedList1)
print(bubblesort(unsortedList1))

stations = {"kone":[set(["JS", "SH", "ZJ"])], "ktwo":set(["JS","AH", "JX"])}    #Dictionary is a hash table

print(stations["kone"][0])
print(stations["ktwo"])

city1 = stations["kone"]
city2 = stations["ktwo"]
print(city1[0] & city2)
