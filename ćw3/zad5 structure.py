"""mamy dwa kopce, jeden min, drugi max, przechowujące te same dane
insert do obydwu w czasie logn
znalezienie elementu min i max w czasie jednostkowym, naprawienie kopca po usunięciu w czasie logn,
natomiast musimy usunac elem max takze z kopca min (i odwrotnie), zatem kazdy element z jednego kopca musi
posiadac referencje do siebie w drugim kopcu"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.min_index = None
        self.max_index = None


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify_max(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    max_index = i
    if l_child <= n - 1 and arr[l_child].key > arr[max_index].key:
        max_index = l_child
    if r_child <= n - 1 and arr[r_child].key > arr[max_index].key:
        max_index = r_child

    if max_index != i:
        arr[i].max_index = max_index
        arr[max_index].max_index = i
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify_max(arr, n, max_index)


def heapify_min(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    min_index = i
    if l_child <= n - 1 and arr[l_child].key < arr[min_index].key:
        min_index = l_child
    if r_child <= n - 1 and arr[r_child].key < arr[min_index].key:
        min_index = r_child

    if min_index != i:
        arr[i].min_index = min_index
        arr[min_index].min_index = i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        heapify_min(arr, n, min_index)


def build_min_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(arr, n, i)
    for j in range(n):
        arr[j].min_index = j
    return arr


def build_max_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify_max(arr, n, i)
    for j in range(n):
        arr[j].max_index = j
    return arr


def insert(max_heap, min_heap, val):
    new = Node(val)

    max_heap.append(new)
    i = len(max_heap) - 1
    new.max_index = i
    while True:
        if i == 0:
            break
        par = parent(i)
        if max_heap[par].key < max_heap[i].key:
            max_heap[par].max_index = i
            max_heap[i].max_index = par
            max_heap[par], max_heap[i] = max_heap[i], max_heap[par]
            i = par
        else:
            break

    min_heap.append(new)
    i = len(min_heap) - 1
    new.min_index = i
    while True:
        if i == 0:
            break
        par = parent(i)
        if min_heap[par].key > min_heap[i].key:
            min_heap[par].min_index = i
            min_heap[i].min_index = par
            min_heap[par], min_heap[i] = min_heap[i], min_heap[par]
            i = par
        else:
            break


def del_max(max_heap, min_heap):
    last = max_heap.pop()
    biggest = max_heap[0]
    max_heap[0] = last
    max_heap[0].max_index = 0
    heapify_max(max_heap, len(max_heap), 0)

    min_idx = biggest.min_index
    last = min_heap.pop()
    if min_idx == len(min_heap):  # it was last
        return
    min_heap[min_idx] = last
    min_heap[min_idx].min_index = min_idx
    while True:
        if min_idx == 0:
            break
        par = parent(min_idx)
        if min_heap[par].key > min_heap[min_idx].key:
            min_heap[par].min_index = min_idx
            min_heap[min_idx].min_index = par
            min_heap[min_idx], min_heap[par] = min_heap[par], min_heap[min_idx]
        else:
            break
        min_idx = par


def del_min(max_heap, min_heap):
    last = min_heap.pop()
    smallest = min_heap[0]
    min_heap[0] = last
    min_heap[0].min_index = 0
    heapify_min(min_heap, len(min_heap), 0)

    max_idx = smallest.max_index
    last = max_heap.pop()
    if max_idx == len(max_heap):  # it was last
        return
    max_heap[max_idx] = last
    max_heap[max_idx].max_index = max_idx
    while True:
        if max_idx == 0:
            break
        par = parent(max_idx)
        if max_heap[par].key < max_heap[max_idx].key:
            max_heap[par].max_index = max_idx
            max_heap[max_idx].max_index = par
            max_heap[max_idx], max_heap[par] = max_heap[par], max_heap[max_idx]
        else:
            break
        max_idx = par


def print_me(arr):
    for elem in arr:
        print(elem.key, end=" ", )
        print("{", elem.max_index, elem.min_index, "}", end=" ")
    print()


if __name__ == '__main__':
    test = [3, 1, 7, 4]
    for q in range(len(test)):
        test[q] = Node(test[q])

    min_h = build_min_heap(test.copy())
    max_h = build_max_heap(test.copy())
    # now ready to go
