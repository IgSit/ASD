def mergesort(arr):
    n = len(arr)
    tmp_arr = [0 for _ in range(n)]
    return merge_sort_algo(arr, tmp_arr, 0, n - 1)


def merge_sort_algo(arr, tmp_arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_algo(arr, tmp_arr, left, mid)
        merge_sort_algo(arr, tmp_arr, mid + 1, right)
        merge(arr, tmp_arr, left, mid, right)
    return arr


def merge(arr, tmp_arr, left, mid, right):
    i = k = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp_arr[k] = arr[i]
            i += 1
        else:
            tmp_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        tmp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        tmp_arr[k] = arr[j]
        j += 1
        k += 1

    for q in range(left, right + 1):
        arr[q] = tmp_arr[q]