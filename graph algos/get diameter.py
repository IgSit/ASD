from collections import deque


def get_diameter(graph):
    n = len(graph)

    def bfs_dist(start):
        queue = deque()
        visited = [False for _ in range(n)]
        distances = [0 for _ in range(n)]
        queue.append((start, 0))
        visited[start] = True

        while queue:
            v, dist = queue.popleft()
            for u in graph[v]:
                if not visited[u]:
                    queue.append((u, dist + 1))
                    visited[u] = True
                    distances[u] = dist + 1
        return distances

    dists = bfs_dist(0)
    x = dists.index(max(dists))
    dists = bfs_dist(x)
    y = dists.index(max(dists))
    return x, y


if __name__ == '__main__':
    test = [[1, 8],
            [0, 2, 3],
            [1, 3],
            [1, 2, 4],
            [3, 5],
            [4, 6],
            [4, 5],
            [9, 8],
            [0, 7, 9],
            [7, 8]]
    print(get_diameter(test))
