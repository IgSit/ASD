class FastListNode:
    def __init__(self, a):
        self.a = a     # przechowywana liczba całkowita
        self.next = []  # lista odsyłaczy do innych elementów; początkowo pusta

    def __str__(self):  # zwraca zawartość węzła w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def add_at_the_beginning(head, num):
    new_head = FastListNode(num)
    if head is None:
        return new_head
    new_head.next.append(head)
    i = 0
    while True:
        try:
            head = head.next[i]
        except IndexError:
            break
        new_head.next.append(head)
        i += 1
    return new_head
