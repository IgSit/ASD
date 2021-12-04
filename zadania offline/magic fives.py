from random import randint
from time import time


def partition(arr, left, right, med):
    for q in range(left, right):  # look for median and put in at the end of array
        if arr[q] == med:
            arr[q], arr[right] = arr[right], arr[q]
            break
    i = left
    for j in range(left, right):
        if arr[j] < arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def magic_fives(arr, left, right, k):
    length = right - left + 1
    if length <= 5:  # not many medians, sort them normally
        bubble_sort(arr, left, right)
        return arr[k]

    i = left
    med_i = left
    while i + 4 <= right:  # until we have "full" fives
        bubble_sort(arr, i, i + 4)
        arr[med_i], arr[i + 2] = arr[i + 2], arr[med_i]
        med_i += 1
        i += 5

    if length % 5 != 0:  # if there is some rest at the end
        bubble_sort(arr, i, right)
        last_len = right - i + 1
        if last_len == 1 or last_len == 2:
            arr[i], arr[med_i] = arr[med_i], arr[i]  # take first as median or lower median
        elif last_len == 3 or last_len == 4:
            arr[i + 1], arr[med_i] = arr[med_i], arr[i + 1]  # take second as median or lower median

    return magic_fives(arr, left, med_i - 1, (med_i - 1) // 2)


def bubble_sort(arr, start, end):
    for c in range(start, end + 1):
        for d in range(c + 1, end + 1):
            if arr[c] > arr[d]:
                arr[c], arr[d] = arr[d], arr[c]


def linear_select(arr, start, end, k):
    if end - start <= 5:  # end of recursion, array has few elements
        bubble_sort(arr, start, end)
        return arr[k]

    m = magic_fives(arr, start, end, k)

    pivot = partition(arr, start, end, m)
    if k < pivot:
        return linear_select(arr, start, pivot - 1, k)  # amount of elements < median is greater than searched index
    elif pivot < k:  # we have to look for result in that group
        return linear_select(arr, pivot + 1, end, k)
    else:  # we are lucky, searched element is our pivot
        return arr[pivot]


def linearselect(arr, k):
    return linear_select(arr, 0, len(arr) - 1, k)


def test_sort():
    rr = (-1000000, 1000000)
    n = 1000000
    m = 10
    print_res = False

    for i in range(m):
        t = [randint(rr[0], rr[1]) for _ in range(n)]
        expected_res = sorted(t)

        """k = randint(0,n-1)"""
        k = 30
        expected = expected_res[k]

        if print_res:
            print('sorted_input:   ', expected_res)

        start = time()
        q = linearselect(t, k)
        stop = time()
        if print_res: print('output:  ', q, ' expected:  ', expected)

        res = 'INCORRECT'
        if q == expected:
            res = 'CORRECT'

        print('result:  ', res)
        print('time:    ', stop - start, '\n')

        if res == 'INCORRECT':
            break


if __name__ == '__main__':
    test_sort()
