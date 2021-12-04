class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def split(head):
    odd = p_odd = Node()
    even = p_even = Node()
    while head is not None:
        if head.value % 2 == 0:
            p_even.next = head
            p_even = p_even.next
        else:
            p_odd.next = head
            p_odd = p_odd.next
        mem = head.next
        head.next = None
        head = mem
    return odd.next, even.next


def display_ll(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


def arr2list(arr):
    head = p = Node()
    for num in arr:
        p.next = Node(num)
        p = p.next
    return head.next


if __name__ == '__main__':
    test = [1, 4, 2, 6, 4, 7]
    test = arr2list(test)
    w, q = split(test)
    display_ll(w)
    display_ll(q)
