class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value


def display_linked_list(head):
    head = head.next
    while head is not None:
        print(head.key, end=" ")
        head = head.next
    print()


def del_max_elem(head):
    p = head.next
    biggest = head.next
    prev = head
    while p.next is not None:
        tmp = p
        p = p.next
        if p.key > biggest.key:
            biggest = p
            prev = tmp
    prev.next = biggest.next
    del biggest
