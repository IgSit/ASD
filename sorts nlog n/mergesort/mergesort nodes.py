class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def display_ll(head):
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


def merge(head1, head2):
    ward = last = Node()
    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            last.next = head1
            mem = head1.next
            head1.next = None
            head1 = mem
        else:
            last.next = head2
            mem = head2.next
            head2.next = None
            head2 = mem
        last = last.next

    if head1 is not None:
        last.next = head1
    else:
        last.next = head2

    head = ward.next
    del ward
    return head


def find_series(curr):
    while curr.next is not None and curr.next.key >= curr.value:
        curr = curr.next
    new_curr = curr.next
    curr.next = None
    return new_curr


def merge_sort(head):
    if head is None or head.next is None:
        return head
    new_head = find_series(head)
    if new_head is None:
        return head
    new_new_head = find_series(new_head)
    head = merge(head, new_head)
    if new_new_head is not None:
        return merge(head, merge_sort(new_new_head))
    return head
