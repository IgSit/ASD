def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    max_index = i
    if l_child < n and arr[l_child] < arr[max_index]:
        max_index = l_child
    if r_child < n and arr[r_child] < arr[max_index]:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def build_min_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, n, i)
    return arr


def check_kth_smallest(arr, k, x):

    def recursive_check(i=0):
        nonlocal found_smaller
        if found_smaller == k:
            return

        l_child = arr[left(i)] if left(i) < n else None
        r_child = arr[right(i)] if right(i) < n else None
        if l_child is not None and l_child < x:
            found_smaller += 1
            recursive_check(left(i))
        if r_child is not None and r_child < x:
            found_smaller += 1
            recursive_check(right(i))
        return

    n = len(arr)
    found_smaller = 0
    if k == 0:
        return arr[0] >= x
    recursive_check()
    return False if found_smaller >= k else True


if __name__ == '__main__':
    test = [1, 4, 6, 7, 3, 5, 2, 1, 6, 8]
    test = build_min_heap(test)
    print(test)
    print(check_kth_smallest(test, 0, 2))
    print(sorted(test))
