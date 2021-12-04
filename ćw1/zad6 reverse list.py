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


def reverse_linked_list(head):
    p = head.next
    prev = head
    prev.next = None
    while p is not None:
        mem = p
        p = p.next
        mem.next = prev
        prev = mem
    new_watch = Node()
    new_watch.next = prev
    return new_watch
