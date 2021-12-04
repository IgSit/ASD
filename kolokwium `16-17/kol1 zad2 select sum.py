from random import randint


def partition(arr, left, right, piv):
    pivot = arr[piv]
    arr[right], arr[piv] = arr[piv], arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right, randint(left, right))
    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)


def select_sum(arr, start, end):
    n = len(arr)
    val_start = quick_select(arr, 0, n - 1, start)
    val_end = quick_select(arr, 0, n - 1, end)

    elem_sum = 0
    for val in arr:
        if val_start <= val <= val_end:
            elem_sum += val
    return elem_sum


if __name__ == '__main__':
    test = [4, 5, 7, 3, 8, 9, 1, 2]
    print(select_sum(test, 1, 4))
    print(sorted(test))
