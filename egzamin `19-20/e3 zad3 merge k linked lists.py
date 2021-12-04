class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


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
    if l_child < n and arr[l_child].val < arr[max_index].val:
        max_index = l_child
    if r_child < n and arr[r_child].val < arr[max_index].val:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def add_to_heap(arr, elem):
    arr.append(elem)
    i = len(arr) - 1
    while True:
        par = parent(i)
        if arr[par].val > arr[i].val:
            arr[par], arr[i] = arr[i], arr[par]
            i = par
        else:
            break
        if i == 0:
            break


def merge_k_sorted(arr):
    k = len(arr)
    kop = []

    for q in range(k):
        add_to_heap(kop, arr[q])

    head = tail = Node()

    while kop:
        tail.next = kop[0]
        tail = tail.next
        if kop[0].next is not None:
            kop[0] = kop[0].next
        else:
            kop[0], kop[len(kop) - 1] = kop[len(kop) - 1], kop[0]
            kop.pop()
        heapify(kop, len(kop), 0)

    tail.next = None
    return head.next
