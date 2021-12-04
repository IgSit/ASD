class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def display_linked_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


def array_to_list(arr):
    if arr is None or arr == []:
        return None
    head = curr = Node(arr[0])
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head


def get_tail_and_len(head):
    cnt = 1  # we do not count last elem
    while head.next is not None:
        head = head.next
        cnt += 1
    return head, cnt


def quicksort(head):
    tail, length = get_tail_and_len(head)
    if length < 2:
        return head
    left_war, right_war = Node(), Node()  # add wardens
    left_war.next = head
    tail.next = right_war
    partition(left_war, right_war)
    p = left_war.next
    while p.next.key is not None:  # remove wardens
        p = p.next
    p.next = None
    new_head = left_war.next
    left_war.next = None
    return new_head


def partition(left_war, right_war):
    pivot = left_war.next
    eq_pivot = pivot  # second pivot to catch all elements equal to pivot to ignore them in further sorting
    curr = pivot.next
    prev = pivot
    pivot_prev = left_war
    if curr is right_war:
        return None
    while curr is not right_war:
        if curr.key < pivot.key:
            prev.next = curr.next
            pivot_prev.next = curr
            pivot_prev = pivot_prev.next
            pivot_prev.next = pivot
            curr = prev.next
        elif curr.key > pivot.key:
            prev = prev.next
            curr = curr.next
        else:  # equality of curr and pivot
            if pivot.next == curr:
                eq_pivot = curr
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr.next = pivot.next
                pivot.next = curr
                curr = prev.next

    if left_war.next is not pivot:
        partition(left_war, pivot)
    if eq_pivot.next is not right_war:
        partition(eq_pivot, right_war)
    return None
