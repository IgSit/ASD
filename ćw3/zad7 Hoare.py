def partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = right + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)
    return arr


if __name__ == '__main__':
    test = [1, 5, 2, 6, 3, 8, 9, 0, 3]
    print(quicksort(test, 0, len(test) - 1))
