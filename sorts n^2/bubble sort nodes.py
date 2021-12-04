class Node:
    def __init__(self, value=None, nxt=None):
        self.next = nxt
        self.value = value


def print_list(head):
    while head is not None:
        print(head.value, "->", end=" ")
        head = head.next
    print("|")


def bubble_sort_list(head):
    head1 = Node("{*}", head)
    anchor = True
    while anchor:
        prev = head1
        curr1 = prev.next
        curr2 = curr1.next
        anchor = False
        while curr2 is not None:
            if curr1.value > curr2.value:
                prev.next = curr2
                curr1.next = curr2.next
                curr2.next = curr1
                prev = curr2
                curr2 = curr1.next
                anchor = True
            else:
                prev = curr1
                curr1 = curr2
                curr2 = curr2.next

    return head1.next


if __name__ == '__main__':
    h = Node(8, Node(1, Node(3, Node(1, Node(3, Node(7, Node(5, Node(8, Node(5, Node(6, Node(4)))))))))))
    print_list(h)
    print_list(bubble_sort_list(h))
