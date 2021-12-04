from random import randint


def partition(a, left, right, itm_gtr):
    piv = randint(left, right)
    pivot = a[piv]
    a[right], a[piv] = a[piv], a[right]
    i = left
    for j in range(left, right):
        if a[j][itm_gtr] < pivot[itm_gtr] or (a[j][itm_gtr] == pivot[itm_gtr] and a[j][itm_gtr - 1] < pivot[itm_gtr - 1]):
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


def quick_select(arr, left, right, val, itm_gtr):
    if left == right:
        return left

    pivot_index = partition(arr, left, right, itm_gtr)
    pivot_val = arr[pivot_index]
    if val == pivot_val:
        return pivot_index
    elif val < pivot_val:
        return quick_select(arr, left, pivot_index - 1, val, itm_gtr)
    else:
        return quick_select(arr, pivot_index + 1, right, val, itm_gtr)


if __name__ == '__main__':
    test = [[1, 3], [1, 2], [1, 1], [2, 2], [2, 3]]
    print(quick_select(test, 0, len(test) - 1, [1, 3], 0))
