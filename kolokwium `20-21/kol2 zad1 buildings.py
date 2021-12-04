# f(i, c) - maksymalna liczba studentow, budując bloki od 0 do i o koszcie <= c
# f(i, c) = max( f(i - 1, c), f( prev(i), c - cost(i) + people(i) )
# prev(i) - ostatni budynek przed i nienachodzący na i

# budynek: (h, a, b, w)

from operator import itemgetter


def students(arr):  # O(n)
    n = len(arr)
    people = [-1 for _ in range(n)]
    for i in range(n):
        people[i] = arr[i][0] * (arr[i][2] - arr[i][1])
    return people


def prev(arr):  # O(n^2)
    n = len(arr)
    last = [-1 for _ in range(n)]
    for i in range(n):
        for k in range(i - 1, -1, -1):
            if arr[k][2] < arr[i][1]:
                last[i] = k
                break
    return last


def buildings(arr, p):  # O(n^2 + np)
    n = len(arr)
    base_arr = arr.copy()  # O(n)
    pos = [-1 for _ in range(n)]
    arr.sort(key=itemgetter(2))  # O(n log n)
    people = students(arr)  # O(n)
    last = prev(arr)  # O(n^2)
    cost = [arr[a][3] for a in range(n)]
    for b in range(n):  # O(n^2)
        elem = arr[b]
        pos[b] = base_arr.index(elem)

    func = [[0 for _ in range(p + 1)] for _ in range(n)]
    for q in range(cost[0], p + 1):
        func[0][q] = people[0]

    for i in range(1, n):  # O(np)
        for c in range(p + 1):
            func[i][c] = func[i - 1][c]
            if cost[i] <= c:
                func[i][c] = max(func[i][c], people[i])
            if last[i] != -1 and c - cost[i] >= 0:
                func[i][c] = max(func[i][c], func[last[i]][c - cost[i]] + people[i])

    max_people, min_cost = 0, p + 1
    for i in range(p + 1):  # O(p)
        if func[n - 1][i] > max_people:
            max_people = func[n - 1][i]
            min_cost = i

    res = []
    i = n - 1
    while max_people != 0:  # O(n)
        if max_people == people[i] and min_cost == cost[i]:
            res.append(pos[i])
            break
        elif min_cost - cost[i] >= 0:
            if func[i][min_cost] == func[last[i]][min_cost - cost[i]] + people[i]:
                res.append(pos[i])
                min_cost -= cost[i]
                max_people -= people[i]
                i = last[i]
            else:
                i -= 1
        else:
            i -= 1

    res.sort()

    return res
