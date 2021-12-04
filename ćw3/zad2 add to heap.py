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
    if l_child < n and arr[l_child] > arr[max_index]:
        max_index = l_child
    if r_child < n and arr[r_child] > arr[max_index]:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def build_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, n, i)
    return arr


def heapsort(arr):
    n = len(arr)
    build_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def add_to_heap(arr, elem):
    arr.append(elem)
    i = len(arr) - 1
    while True:
        par = parent(i)
        if arr[par] < arr[i]:
            arr[par], arr[i] = arr[i], arr[par]
            i = par
        else:
            break
        if i == 0:
            break


if __name__ == '__main__':
    test = [1, 5, 2, 7, 8, 4, 0]
    heap = build_heap(test)
    print(heap)
    add_to_heap(heap, 7)
    print(heap)
    print(heapsort(heap))
