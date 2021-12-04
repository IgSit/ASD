from random import randint


def quicksort(arr, left, right, itm_getter):
    while left < right:
        pivot = partition(arr, left, right, itm_getter)
        if pivot - left < right - pivot:
            quicksort(arr, left, pivot - 1, itm_getter)
            left = pivot + 1
        else:
            quicksort(arr, pivot + 1, right, itm_getter)
            right = pivot - 1
    return arr


def partition(a, left, right, itm_gtr):
    piv = randint(left, right)
    pivot = a[piv]
    a[right], a[piv] = a[piv], a[right]
    i = left
    if itm_gtr == 0:
        s_i = 1
    else:
        s_i = 0
    for j in range(left, right):
        if a[j][itm_gtr] < pivot[itm_gtr] or (a[j][itm_gtr] == pivot[itm_gtr] and a[j][s_i] > pivot[s_i]):
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


def dominant_points(arr):
    n = len(arr)
    arr = quicksort(arr, 0, n - 1, 1)  # sort by y - O(n * log n)
    res = [arr.pop()]
    curr_x = res[0][0]
    curr_y = res[0][1]
    for i in range(n - 2, -1, -1):  # O(n)
        if not (arr[i][0] < curr_x and arr[i][1] < curr_y):
            if arr[i][0] > curr_x:
                curr_x = arr[i][0]
            res.append(arr[i])
    return res


if __name__ == '__main__':
    test = [[2, 3], [2, 4], [3, 1], [4, 3], [4, 5], [6, 3], [8, 3], [5, 2], [7, 2], [7, 0], [8, 1], [10, 2], [11, 3]]
    print(dominant_points(test))
