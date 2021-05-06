"""
Thuật toán bubble sort
"""
import random as rd
import time
import matplotlib.pyplot as plt
def bubbleSort(key):
    n = len(key)
    for i in range(n -1 ):
        for j in range(0,n-i- 1):
            if key[j] > key[j+1]:
                key[j] , key[j+1] = key[j+1], key[j]
"""
Thuật toán selection sort
"""
def SelectionSort(key):
    n = len(key)
    for i in range(n-1):
        k = i
        for j in range(i+1 ,n):
            if(key[k] > key[j]):
                k = j
        if (k!= i):
            key[i], key[k] = key[k] , key[i]
"""
Thuật toán insert Sort
"""
def InsertSort(key):
    n = len(key)
    for i in range(1,n):
        vt = i -1
        x = key[i]
        while(vt>=0 and key[vt] > x):
            key[vt +1] = key[vt]
            vt -= 1
        key[vt+1] = x
"""
Thuat toan merge sort
"""

def Merge(key, left, mid, right):
    i = left
    j = mid +1
    key1 = list()
    while (i <= mid and j <= right):
        if (key[i] > key[j]):
            key1.append(key[j])
            j += 1
        else:
            key1.append(key[i])
            i += 1
    if (i > mid):
        for a in range(j, right +1):
            key1.append(key[a])
    else:
        for a in range(i,mid+1):
            key1.append(key[a])
    key[left:right+1] = key1


def MergeSort(key, left, right):
    if left < right:
        mid = int((left + right) / 2)
        MergeSort(key, left, mid)
        MergeSort(key, mid + 1, right)
        Merge(key, left, mid, right)
"""
Ham ve do thi
"""
def graphic():
    nPoints = 20
    timesBubble = list()
    timesSelection = list()
    timesInsert = list()
    timesMerge = list()
    n = 1000
    listPoints = list()
    for i in range(nPoints):
        #key = rd.sample(range(n), n)
        key1 = rd.sample(range(n), n)
        key2 = rd.sample(range(n), n)
        key3 = rd.sample(range(n), n)
        key4 = rd.sample(range(n), n)
        start = time.time()
        bubbleSort(key1)
        end = time.time()
        timesBubble.append(end - start)
        start = time.time()
        SelectionSort(key2)
        end = time.time()
        timesSelection.append(end - start)
        start = time.time()
        InsertSort(key3)
        end = time.time()
        timesInsert.append(end - start)
        start = time.time()
        MergeSort(key4, 0, n-1)
        end = time.time()
        timesMerge.append(end - start)
        listPoints.append(n)
        n+=200
    plt.figure(figsize= (10,10))
    plt.plot(listPoints, timesBubble, 'go-', label='Bubble Sort')
    plt.plot(listPoints, timesSelection, 'ro-', label='Selection Sort')
    plt.plot(listPoints, timesInsert, 'bD-', label='Insert Sort')
    plt.plot(listPoints, timesMerge, 'g^-', label='Merge Sort')
    plt.legend(loc = 'best')
    plt.title('Investigate the runtime of sorting algorithms')
    plt.xlabel('Data set size')
    plt.ylabel('Running time (s)')
    plt.show()
graphic()