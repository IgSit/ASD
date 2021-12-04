def merge_sort(arr):
    n = len(arr)
    curr_len = 1
    while curr_len < n - 1:
        left = 0
        while left < n - 1:
            mid = min(left + curr_len - 1, n - 1)
            if left + 2 * curr_len - 1 < n - 1:
                right = left + 2 * curr_len - 1
            else:
                right = n - 1
            merge(arr, left, mid, right)
            left += curr_len * 2
        curr_len *= 2
    return arr


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    l_arr = [0] * n1
    r_arr = [0] * n2
    for i in range(0, n1):
        l_arr[i] = arr[left + i]
    for i in range(0, n2):
        r_arr[i] = arr[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if l_arr[i] > r_arr[j]:
            arr[k] = r_arr[j]
            j += 1
        else:
            arr[k] = l_arr[i]
            i += 1
        k += 1

    while i < n1:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    print(merge_sort([1, 4, 2, 6]))
