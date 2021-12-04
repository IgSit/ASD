class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def display_ll(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


def arr2list(arr):
    if arr is None or arr == []:
        return Node()
    head = Node(arr[0])
    last = head
    for i in range(1, len(arr)):
        last.next = Node(arr[i])
        last = last.next
    return head


def merge(head1, head2):
    ward = Node()
    last = ward
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

    new_head = ward.next
    del ward
    return new_head


def find_series(head):
    while head.next and head.value <= head.next.key:
        head = head.next
    new_head = head.next
    head.next = None
    return new_head


def mergesort(head):
    if head is None or head.next is None:
        return head

    new_head = find_series(head)
    if new_head is None:
        return head

    newer_head = find_series(new_head)
    merged = merge(head, new_head)
    if newer_head is not None:
        return merge(merged, mergesort(newer_head))
    else:
        return merged


if __name__ == '__main__':
    test = [2, 0, 1, 1]
    test = arr2list(test)
    display_ll(test)
    display_ll(mergesort(test))
