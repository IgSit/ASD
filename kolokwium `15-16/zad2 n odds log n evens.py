from math import log2, ceil, floor
from random import randint


def partition(arr, left, right):
    rand_index = randint(left, right)
    arr[right], arr[rand_index] = arr[rand_index], arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]:
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


def sort_array(arr):
    n = len(arr)
    n1 = floor(n - log2(n))
    n2 = ceil(log2(n))
    odds = [0] * n1
    evens = [0] * n2

    odd_i = even_i = 0
    for num in arr:  # O(n)
        if num % 2 == 1:
            odds[odd_i] = num  # already sorted
            odd_i += 1
        else:
            evens[even_i] = num
            even_i += 1

    evens = quicksort(evens, 0, n2 - 1)  # O(log n * log(log n))

    odd_i = even_i = i = 0  # O(n)
    while odd_i <= n1 - 1 and even_i <= n2 - 1:
        if odds[odd_i] < evens[even_i]:
            arr[i] = odds[odd_i]
            odd_i += 1
        else:
            arr[i] = evens[even_i]
            even_i += 1
        i += 1

    while odd_i <= n1 - 1:
        arr[i] = odds[odd_i]
        odd_i += 1
        i += 1
    while even_i <= n2 - 1:
        arr[i] = evens[even_i]
        even_i += 1
        i += 1

    return arr


if __name__ == '__main__':
    test = [11, 33, 66, 69, 75, 80, 91, 2]
    print(sort_array(test))
    print(sorted(test))
