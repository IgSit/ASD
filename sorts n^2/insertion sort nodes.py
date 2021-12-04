class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def insertion_sort(head):
    new_head = Node()
    while head is not None:
        mem = head.next
        head.next = None
        new_head = insert(new_head, head)
        head = mem
    return new_head.next


def insert(head, node):
    p = head
    while p.next is not None and p.next.key < node.key:
        p = p.next
    node.next = p.next
    p.next = node
    return head


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
    test = [4, 3, 7, 1, 0, 2]
    display_ll(insertion_sort(arr2list(test)))
