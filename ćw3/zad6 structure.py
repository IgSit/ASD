"""utrzymujemy dwa kopce, jeden min, drugi max. Sprawdzamy obecną medianę (O(1)) i jesli element jest mniejszy
 od mediany, to dodajemy go do kopca max: kopiec max przechowuje wartości mniejsze od mediany. Jeśli kopce są
 niezrównoważone ( różnica długości 2), to bierzemy root z wiekszego kopca, naprawiamy go, a dany root wstawiamy
 do drugiego kopca"""


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def max_heapify(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    max_index = i
    if l_child < n and arr[l_child] > arr[max_index]:
        max_index = l_child
    if r_child < n and arr[r_child] > arr[max_index]:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        max_heapify(arr, n, max_index)


def build_max_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        max_heapify(arr, n, i)
    return arr


def add_to_max_heap(arr, elem):
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


def min_heapify(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    min_index = i
    if l_child < n and arr[l_child] < arr[min_index]:
        min_index = l_child
    if r_child < n and arr[r_child] < arr[min_index]:
        min_index = r_child
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        min_heapify(arr, n, min_index)


def build_min_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        min_heapify(arr, n, i)
    return arr


def add_to_min_heap(arr, elem):
    arr.append(elem)
    i = len(arr) - 1
    while True:
        par = parent(i)
        if arr[par] > arr[i]:
            arr[par], arr[i] = arr[i], arr[par]
            i = par
        else:
            break
        if i == 0:
            break


def insert(min_heap, max_heap, elem):
    if len(max_heap) > len(min_heap):
        median = max_heap[0]
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
    else:
        median = (min_heap[0] + max_heap[0]) / 2

    if elem > median:
        add_to_min_heap(min_heap, elem)
    else:
        add_to_max_heap(max_heap, elem)

    if abs(len(max_heap) - len(min_heap)) == 2:
        if len(max_heap) > len(min_heap):
            swap_me = max_heap[0]
            last = max_heap.pop()
            max_heap[0] = last
            max_heapify(max_heap, len(max_heap), 0)
            add_to_min_heap(min_heap, swap_me)
        else:
            swap_me = min_heap[0]
            last = min_heap.pop()
            min_heap[0] = last
            min_heapify(min_heap, len(min_heap), 0)
            add_to_max_heap(max_heap, swap_me)


def remove_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        min_heap[0] = min_heap.pop()
        min_heapify(min_heap, len(min_heap), 0)
    elif len(min_heap) < len(max_heap):
        max_heap[0] = max_heap.pop()
        max_heapify(max_heap, len(max_heap), 0)
    else:
        min_heap[0] = min_heap.pop()
        min_heapify(min_heap, len(min_heap), 0)
        max_heap[0] = max_heap.pop()
        max_heapify(max_heap, len(max_heap), 0)


if __name__ == '__main__':
    min_h = [1]
    max_h = [2]
    array = [3, 5, 7, 9]
    for element in array:
        insert(min_h, max_h, element)
        print("Max heap - lower than median: ", max_h)
        print("Min heap - greater than median", min_h)
        print("------------")
    remove_median(min_h, max_h)
    print("Max heap - lower than median: ", max_h)
    print("Min heap - greater than median", min_h)
