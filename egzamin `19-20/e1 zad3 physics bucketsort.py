from math import log


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int(elem // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1


def fast_sort(arr, a):
    n = len(arr)
    for i in range(n):  # O(n)
        arr[i] = log(arr[i], a)

    bucket_sort(arr, 1)  # O(n)

    for i in range(n):
        arr[i] = a ** arr[i]  # O(n)

    return arr
