class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value


def get_tail_and_len(head):
    cnt = 1  # we do not count last elem
    while head.next is not None:
        head = head.next
        cnt += 1
    return head, cnt


def qsort(head):
    tail, length = get_tail_and_len(head)
    if length < 2:  # sorted
        return head

    left_war, right_war = Node(), Node()  # add wardens
    left_war.next = head
    tail.next = right_war

    partition(left_war, right_war)  # actual sorting

    p = left_war.next  # remove wardens
    while p.next.key is not None:
        p = p.next
    p.next = None
    new_head = left_war.next
    left_war.next = None  # assume garbage collector is working properly
    return new_head


def partition(left_war, right_war):
    pivot = left_war.next
    eq_pivot = pivot  # second pivot to catch all elements equal to pivot to ignore them in further sorting
    curr = pivot.next  # (these elements will be put between pivot and eq_pivot)
    prev = pivot
    pivot_prev = left_war

    if curr is right_war:
        return None

    while curr is not right_war:
        if curr.key < pivot.key:  # put it right before pivot
            prev.next = curr.next
            pivot_prev.next = curr
            pivot_prev = pivot_prev.next
            pivot_prev.next = pivot
            curr = prev.next

        elif curr.key > pivot.key:  # just skip
            prev = prev.next
            curr = curr.next

        else:  # equality of curr and pivot

            if pivot.next == curr:  # first repeated element equal to pivot
                eq_pivot = curr  # use second pivot
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next  # put it just after pivot
                curr.next = pivot.next
                pivot.next = curr
                curr = prev.next

    if left_war.next is not pivot:
        partition(left_war, pivot)
    if eq_pivot.next is not right_war:
        partition(eq_pivot, right_war)
    return None
