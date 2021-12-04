# algorytm: zaczynamy uzupełniać od ostatniego dnia, rozważając te zadania, które kończą się ostatniego dnia
# trzymamy je w maxheapie i bierzemy największy
# następnie przechodzimy do dnia poprzedniego i do kopca dodajemy zadania, które się wtedy kończą
# dzięki temu zawsze bierzemy najlepiej płatne zadanie z wszystkich dostępnych

from operator import itemgetter


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(arr, n, i):
    l_child = left(i)
    r_child = right(i)
    max_index = i
    if l_child < n and arr[l_child][0] > arr[max_index][0]:
        max_index = l_child
    if r_child < n and arr[r_child][0] > arr[max_index][0]:
        max_index = r_child
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)


def build_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, n, i)
    return arr


def add_to_heap(arr, elem):
    arr.append(elem)
    i = len(arr) - 1
    while True:
        par = parent(i)
        if arr[par][0] < arr[i][0]:
            arr[par], arr[i] = arr[i], arr[par]
            i = par
        else:
            break
        if i == 0:
            break


def choosing_tasks(profits, deadlines):
    last_day = max(deadlines)
    n = len(profits)
    arr = [[profits[i], deadlines[i]] for i in range(n)]
    arr.sort(key=itemgetter(1))
    res = [-1] * (last_day + 1)
    i = n - 1
    task_heap = []
    while last_day != -1:
        while arr[i][1] == last_day:
            add_to_heap(task_heap, arr[i])
            i -= 1
            if i == - 1:
                break

        res[last_day] = task_heap[0]
        k = len(task_heap)
        task_heap[0], task_heap[k - 1] = task_heap[k - 1], task_heap[0]
        task_heap.pop()
        heapify(task_heap, k - 1, 0)

        if i == -1:
            break
        last_day -= 1
    return res


if __name__ == '__main__':
    t = [4, 6, 7, 5, 2, 1, 7]
    d = [0, 3, 2, 1, 3, 0, 3]
    print(choosing_tasks(t, d))
