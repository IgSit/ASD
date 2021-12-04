from random import randint
from math import sqrt
from copy import deepcopy


def partition(arr, left, right):
    rand_index = randint(left, right)
    arr[right], arr[rand_index] = arr[rand_index], arr[right]
    i = left
    for j in range(left, right):
        if arr[j][1] <= arr[right][1]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksort(arr, left, right):
    while left < right:
        pivot = partition(arr, left, right)
        if pivot - left < right - pivot:
            quicksort(arr, left, pivot - 1)
            left = pivot + 1
        else:
            quicksort(arr, pivot + 1, right)
            right = pivot - 1
    return arr


def sum_sort(arr):
    n2 = len(arr)
    n = int(sqrt(n2))

    buckets = [[q, 0] for q in range(n)]
    for i in range(n2):  # O(n^2)
        index = i // n
        buckets[index][1] += arr[i]

    buckets = quicksort(buckets, 0, n - 1)  # O(n log n)
    i = 0
    tmp_arr = deepcopy(arr)
    for j in range(n):
        index = buckets[j][0] * n
        for k in range(n):
            arr[i] = tmp_arr[index]
            i += 1
            index += 1
    return arr


if __name__ == '__main__':
    test = [1, 3, 5, 3, 3, 2, 6, 7, 8]
    print(sum_sort(test))
