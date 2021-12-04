from collections import deque


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


class PriorityQueue:  # biggest priority value means the most important element, that is done first
    def __init__(self):
        self.queue = []

    def len(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def print(self):
        print(self.queue)

    def add(self, elem, priority):
        self.queue.append([elem, priority])
        i = len(self.queue) - 1
        while True:
            if i == 0:
                break
            par = parent(i)
            if self.queue[par][1] < self.queue[i][1]:
                self.queue[par], self.queue[i] = self.queue[i], self.queue[par]
                i = par
            else:
                break

    def pop(self):

        def heapify(queue, n, i):
            l_child = left(i)
            r_child = right(i)
            max_index = i
            if l_child <= n - 1 and queue[l_child][1] > queue[max_index][1]:
                max_index = l_child
            if r_child <= n - 1 and queue[r_child][1] > queue[max_index][1]:
                max_index = r_child
            if max_index != i:
                queue[i], queue[max_index] = queue[max_index], queue[i]
                heapify(queue, n, max_index)

        length = self.len()
        self.queue[0], self.queue[length - 1] = self.queue[length - 1], self.queue[0]
        mem = self.queue.pop()
        heapify(self.queue, length - 1, 0)
        return mem


def count_oil(arr):
    n = len(arr[0])
    m = len(arr)

    oil = [0 for _ in range(n)]

    for j in range(n):
        for i in range(m):
            if arr[i][j] != 0:
                partial = 0
                queue = deque()
                queue.append([i, j])
                while queue:
                    a, b = queue.popleft()
                    partial += arr[a][b]
                    arr[a][b] = 0
                    moves = [(a - 1, b), (a, b + 1), (a + 1, b), (a, b - 1)]
                    for w, k in moves:
                        if 0 <= w <= m - 1 and 0 <= k <= n - 1 and arr[w][k]:
                            queue.append([w, k])

                arr[i][j] = partial

    for i in range(n):
        oil[i] = sum(arr[r][i] for r in range(m))
    return oil


def plan_route(arr):
    dist = len(arr[0]) - 1
    oil = count_oil(arr)
    petrol = oil[0]
    stops = [0]
    points = PriorityQueue()
    end = 0
    while petrol < dist:
        for k in range(end + 1, petrol + 1):
            points.add(k, oil[k])
        end += petrol

        stop, add_petrol = points.pop()
        stops.append(stop)
        petrol += add_petrol

    stops.sort()
    return stops
