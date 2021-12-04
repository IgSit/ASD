class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value


def insert_node(head, node):  # insert as sorted element
    p = head
    while p.next is not None and p.next.key < node.key:
        p = p.next
    node.next = p.next
    p.next = node
    return head


def display_linked_list(head):
    head = head.next
    while head is not None:
        print(head.key, end=" ")
        head = head.next
    print()


def arr2list(arr):
    ward = Node()
    tail = ward
    for elem in arr:
        tail.next = Node(elem)
        tail = tail.next
    return ward