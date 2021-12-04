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


def test_sort():
    rr = (-1000, 1000)
    n = 50
    m = 7
    print_res = True

    for i in range(m):
        t = [randint(rr[0], rr[1]) for _ in range(n)]
        expected_res = sorted(t)

        k = randint(0, n-1)

        expected = expected_res[k]

        if print_res:
            print('sorted_input:   ', expected_res)

        q = quick_select(t, 0, len(t) - 1, k)
        if print_res:
            print('output:  ', q, ' expected:  ', expected)

        res = 'INCORRECT'
        if q == expected:
            res = 'CORRECT'

        print('result:  ', res)

        if res == 'INCORRECT':
            break


if __name__ == '__main__':
    test = [1, 2, 6, 3, 2, 5, 7, 4, 9]
    print(quick_select(test, 0, len(test) - 1, 4))
    print(test)
