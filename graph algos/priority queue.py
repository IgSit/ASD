def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


class PriorityQueue:  # smallest priority value means the most important element, that is done first
    def __init__(self):
        self.queue = []

    def len(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def print(self):
        print(self.queue)

    def add(self, elem, priority):
        self.queue.append((elem, priority))
        i = len(self.queue) - 1
        while True:
            if i == 0:
                break
            par = parent(i)
            if self.queue[par][1] > self.queue[i][1]:
                self.queue[par], self.queue[i] = self.queue[i], self.queue[par]
                i = par
            else:
                break

    def pop(self):

        def heapify(queue, n, i):
            l_child = left(i)
            r_child = right(i)
            max_index = i
            if l_child <= n - 1 and queue[l_child][1] < queue[max_index][1]:
                max_index = l_child
            if r_child <= n - 1 and queue[r_child][1] < queue[max_index][1]:
                max_index = r_child
            if max_index != i:
                queue[i], queue[max_index] = queue[max_index], queue[i]
                heapify(queue, n, max_index)

        length = self.len()
        self.queue[0], self.queue[length - 1] = self.queue[length - 1], self.queue[0]
        mem = self.queue.pop()
        heapify(self.queue, length - 1, 0)
        return mem


if __name__ == '__main__':
    test = PriorityQueue()
    test.add(5, 1)
    test.add(3, 2)
    test.add(6, 0)
    test.add(7, 5)
    test.add(5, 4)
    while not test.is_empty():
        print(test.pop())
