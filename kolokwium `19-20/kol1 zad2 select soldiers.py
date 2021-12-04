from random import randint


def partition(arr, left, right, piv):
    pivot = arr[piv]
    arr[right], arr[piv] = arr[piv], arr[right]
    i = left
    for j in range(left, right):
        if arr[j] >= pivot:
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


def section(arr, p, q):
    n = len(arr)
    highest = quick_select(arr, 0, n - 1, p)
    shortest = quick_select(arr, 0, n - 1, q)
    res_section = [0 for _ in range(q - p + 1)]
    idx = 0
    for val in arr:
        if shortest <= val <= highest:
            res_section[idx] = val
            idx += 1
            if idx == q - p + 1:  # we can have many equal heights that pass our condition
                break
    return res_section


if __name__ == '__main__':
    test = [174, 135, 167, 189, 190, 145, 178, 176, 189, 176, 176, 156]
    print(section(test, 0, 5))
    print(sorted(test, reverse=True))
