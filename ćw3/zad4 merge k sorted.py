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


def merge_lists(arr):
    while len(arr) > 1:
        k = len(arr)
        i = merged_i = 0
        while i + 1 <= k - 1:
            arr[merged_i] = merge(arr[i], arr[i + 1])
            i += 2
            merged_i += 1
        if i <= k - 1:
            arr[merged_i] = arr[i]
            merged_i += 1
        arr = arr[:merged_i]
    return arr[0]


if __name__ == '__main__':
    e0 = array_to_list([1, 2, 3, 4])
    e1 = array_to_list([2, 4, 6, 7])
    e2 = array_to_list([3, 5])
    e3 = array_to_list([4, 8, 9])
    e4 = array_to_list([5, 5])
    test = [e0, e1, e2, e3, e4]
    display_ll(merge_lists(test))
