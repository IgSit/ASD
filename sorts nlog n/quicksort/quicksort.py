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


if __name__ == '__main__':
    test = ["avb", "ac", "acf", "aa", "a"]
    print(quicksort(test, 0, len(test) - 1))
