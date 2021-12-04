class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def arr2list(arr):
    mem = head = Node()
    for num in arr:
        head.next = Node(num)
        head = head.next
    return mem.next


def display_ll(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


def insert(head, node):
    if head.key > node.key:
        node.next = head
        return node
    p = head
    while p.next is not None and p.next.key < node.key:
        p = p.next
    node.next = p.next
    p.next = node
    return head


def fix_sort(head):
    if head is None or head.next is None:
        return head
    p = head
    prev = head
    curr = head.next
    further = curr.next
    if prev.value > curr.key <= further.key:  # prev is bad - first elem
        p = p.next
        return insert(p, prev)
    if further is None:  # two elements that are sorted
        return p
    while prev.value <= curr.key <= further.key:
        prev = prev.next
        curr = curr.next
        further = further.next
        if further is None:
            return p
    if prev.value <= further.key < curr.key:  # curr is bad
        prev.next = curr.next
        curr.next = None
        return insert(p, curr)
    if further.key < curr.key:  # further is bad
        curr.next = further.next
        further.next = None
        return insert(p, further)


if __name__ == '__main__':
    q = arr2list([3, 3, 4, 5, 6, 7, 8, 9])
    display_ll(fix_sort(q))
