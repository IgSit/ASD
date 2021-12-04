from operator import itemgetter
from math import inf


def min_break_tasks(tasks, t):  # O(nt + n^2)
    tasks.sort(key=itemgetter(1))
    n = len(tasks)

    prev = [-1 for _ in range(n)]
    # pierwszy od końca nienachodzący przedział
    for x in range(n):
        for y in range(x - 1, -1, -1):
            m, _ = tasks[x]
            _, f = tasks[y]
            if f <= m:
                prev[x] = y
                break

    last = [[-1 for _ in range(t + 1)] for _ in range(n)]
    # indeks ostatniego zadania, które mamy w func[i][k] jako najlepszy wynik so far

    func = [[inf for _ in range(t + 1)] for _ in range(n)]
    for q in range(n):
        func[q][0] = 0
        func[q][1] = 0
        last[q][1] = q

    for i in range(1, n):
        for k in range(2, t + 1):
            func[i][k] = func[i - 1][k]
            if prev[i] != -1:
                if last[prev[i]][k - 1] != -1:
                    u, v = tasks[last[prev[i]][k - 1]]
                    o, p = tasks[i]
                    if func[prev[i]][k - 1] + o - v < func[i][k]:
                        func[i][k] = func[prev[i]][k - 1] + o - v
                        last[i][k] = i

    return func[n - 1][t]


if __name__ == '__main__':
    tas = [[1, 3], [3, 5], [6, 8], [9, 10]]
    print(min_break_tasks(tas, 3))
