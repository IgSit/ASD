from math import inf


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


def dijkstra(graph, x, y):  # find shortest path from x to y - neighbourhood list implementation
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [0 for _ in range(n)]
    par = [-1 for _ in range(n)]
    queue = PriorityQueue()
    dist[x] = inf
    for i in range(n):
        queue.add(i, dist[i])

    while not queue.is_empty():
        v, _ = queue.pop()
        if visited[v]:
            continue
        visited[v] = True

        for vertex, capacity in graph[v]:
            alter = min(dist[v], capacity)
            if alter > dist[vertex] and not visited[vertex]:
                dist[vertex] = alter
                par[vertex] = v
                queue.add(vertex, dist[vertex])

    return get_path(par, y)


def get_path(par, y):
    res = []
    while par[y] != -1:
        res.append(y)
        y = par[y]
    res.append(y)
    res.reverse()
    return res


if __name__ == '__main__':
    test = [
        [(1, 4), (2, 3)],
        [(0, 4), (2, 1), (3, 2)],
        [(0, 3), (1, 1), (3, 4), (4, 3)],
        [(1, 2), (2, 4), (4, 2), (5, 1)],
        [(2, 3), (3, 2), (5, 6)],
        [(3, 1), (4, 6)]
        ]

    print(dijkstra(test, 0, 5))
