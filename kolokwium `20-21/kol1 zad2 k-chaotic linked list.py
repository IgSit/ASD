class Node:
    def __init__(self, value):
        self.value = value
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
    if l_child < n and arr[l_child].value < arr[max_index].value:
        max_index = l_child
    if r_child < n and arr[r_child].value < arr[max_index].value:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def add_to_heap(arr, elem):
    arr.append(elem)
    i = len(arr) - 1
    while True:
        par = parent(i)
        if arr[par].value > arr[i].value:
            arr[par], arr[i] = arr[i], arr[par]
            i = par
        else:
            break
        if i == 0:
            break


def k_sort(head, k):
    if k == 0:
        return head
    wid = [head]
    head = head.next
    for _ in range(k):
        add_to_heap(wid, head)
        head = head.next
    new_head = Node("Kill me")
    tail = new_head
    while wid:
        n = len(wid)
        wid[0], wid[n - 1] = wid[n - 1], wid[0]
        tail.next = wid.pop()
        tail = tail.next
        heapify(wid, n - 1, 0)

        if head is not None:
            add_to_heap(wid, head)
            head = head.next

    tail.next = None
    return new_head.next


if __name__ == '__main__':
    pass
