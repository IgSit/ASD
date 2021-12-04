from copy import deepcopy


def quick_sort(arr, item_getter):
    return quicksort(arr, 0, len(arr) - 1, item_getter)


def quicksort(arr, left, right, item_getter):
    while left < right:
        pivot = partition(arr, left, right, item_getter)
        if pivot - left < right - pivot:
            quicksort(arr, left, pivot - 1, item_getter)
            left = pivot + 1
        else:
            quicksort(arr, pivot + 1, right, item_getter)
            right = pivot - 1
    return arr


def partition(arr, left, right, itm_gtr):
    i = left
    for j in range(left, right):
        if (arr[j][itm_gtr] < arr[right][itm_gtr]) or (arr[j][itm_gtr] == arr[right][itm_gtr] and arr[j][itm_gtr - 1] < arr[right][itm_gtr - 1]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def inclusions(arr):
    sort_by_starts = quick_sort(deepcopy(arr), 0)
    sort_by_ends = quick_sort(arr, 1)
    max_res = 0
    res = None
    for i in range(len(arr)):
        interval = arr[i]
        g = max(bin_search(sort_by_ends, interval, 1, 0, len(arr) - 1), 0)
        f = max(bin_search(sort_by_starts, interval, 0, 0, len(arr) - 1), 0)
        if g - f > max_res:
            max_res = g - f
            res = interval
    return res


def bin_search(arr, interval, itm_gtr, left, right):
    if left <= right:
        curr_ind = (left + right) // 2
        if arr[curr_ind] == interval:
            return curr_ind
        elif arr[curr_ind][itm_gtr] < interval[itm_gtr] or (arr[curr_ind][itm_gtr] == interval[itm_gtr] and arr[curr_ind][itm_gtr - 1] < interval[itm_gtr - 1]):
            return bin_search(arr, interval, itm_gtr, curr_ind + 1, right)
        else:
            return bin_search(arr, interval, itm_gtr, left, curr_ind - 1)


if __name__ == '__main__':
    test = [[1, 4], [2, 4], [1, 3], [1, 2]]
    print(inclusions(test))
