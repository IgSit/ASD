from math import inf


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def display_ll(head):
    head = head.next
    while head is not None:
        print(head.key, end=" --> ")
        head = head.next
    print()


def arr2list(arr):
    ward = Node()
    tail = ward
    for elem in arr:
        tail.next = Node(elem)
        tail = tail.next
    return ward


def insertion_sort(head, tail):
    new_head = Node()
    curr = head
    while curr is not None:
        mem = curr.next
        curr.next = None
        new_head, tail = insert(new_head, tail, curr)
        curr = mem
    return new_head.next, tail


def insert(head, tail, node):
    p = head
    while p.next is not None and p.next.key > node.key:
        p = p.next
    node.next = p.next
    p.next = node
    if node.next is None:
        tail = node
    return head, tail


def bucket_sort(head):
    p = head.next
    n = 0
    min_val = inf
    max_val = -inf
    while p is not None:
        if p.key > max_val:
            max_val = p.key
        if p.key < min_val:
            min_val = p.key
        p = p.next
        n += 1

    buckets_head = [None for _ in range(n)]
    buckets_tail = [None for _ in range(n)]
    interval = (max_val - min_val) / n if min_val * max_val > 0 else (max_val + abs(min_val)) / n

    curr = head.next
    while curr is not None:
        index = int((curr.value - min_val) // interval) if int((curr.value - min_val) // interval) <= n - 1 else n - 1

        if buckets_head[index] is None:
            buckets_head[index] = curr
            buckets_tail[index] = curr
        else:
            buckets_tail[index].next = curr
            buckets_tail[index] = buckets_tail[index].next

        mem = curr.next
        curr.next = None
        curr = mem

    buckets_head[n - 1], buckets_tail[n - 1] = insertion_sort(buckets_head[n - 1], buckets_tail[n - 1])
    tail = buckets_tail[n - 1]
    i = n - 2
    while i >= 0:
        buckets_head[i], buckets_tail[i] = insertion_sort(buckets_head[i], buckets_tail[i])
        if buckets_head[i] is not None:
            tail.next = buckets_head[i]
            tail = buckets_tail[i]
        i -= 1
    res_head = Node()
    res_head.next = buckets_head[n - 1]
    return res_head


if __name__ == '__main__':
    test = [1, 5, 4, 3, 2, 2.5, 3.5, 3.6, 3.4, 3.9, 4.1, 2.1, 1.1, 0.9]
    w = arr2list(test)
    display_ll(bucket_sort(w))
