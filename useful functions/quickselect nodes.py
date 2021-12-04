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
        return Node()
    head = curr = Node()
    for i in range(len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    curr.next = Node()
    return head, curr.next


def partition(left_war, right_war):
    pivot = left_war.next
    k = 0
    curr = pivot.next
    prev = pivot
    pivot_prev = left_war
    if curr is right_war:
        return k, pivot
    while curr is not right_war:
        if curr.key < pivot.key:
            prev.next = curr.next
            pivot_prev.next = curr
            pivot_prev = pivot_prev.next
            pivot_prev.next = pivot
            curr = prev.next
            k += 1
        else:
            prev = prev.next
            curr = curr.next
    return k, pivot


def quick_select(left_war, right_war, k):
    if left_war == right_war:
        return left_war.key

    pivot_index, pivot = partition(left_war, right_war)
    if k == pivot_index:
        return pivot.key
    elif k < pivot_index:
        return quick_select(left_war, pivot, k)
    else:
        return quick_select(pivot, right_war, k)


if __name__ == '__main__':
    test = [2, 1, 0, 3, 6, 1]
    h, t = array_to_list(test)
    print(quick_select(h, t, 1))
    print(sorted(test))
