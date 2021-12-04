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


def every_num_is_a_sum(arr):
    n = len(arr)
    arr = quicksort(arr, 0, n - 1)
    for k in range(n):
        i, j = 0, n - 1
        is_sum = False
        while i < j:
            if i == k:
                i += 1
            if j == k:
                j -= 1
            if arr[i] + arr[j] == arr[k]:
                is_sum = True
                break
            if arr[i] + arr[j] < arr[k]:
                i += 1
            elif arr[i] + arr[j] > arr[k]:
                j -= 1
        if not is_sum:
            return False
    return True


if __name__ == '__main__':
    test = [1, 1, 2, 3, 0, -1, -1]
    print(every_num_is_a_sum(test))
