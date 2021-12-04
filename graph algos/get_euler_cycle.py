def EulerCycle(graph):

    def DFSVisit(u):
        nonlocal graph, stack
        for i in graph[u]:
            graph[u].remove(i)
            graph[i].remove(u)
            stack.append(i)
            DFSVisit(i)
        if len(graph[u]) == 0:
            cycle.append(stack.pop())

    stack = []
    cycle = []
    for v in range(len(graph)):
        if len(graph[v]) > 0:
            stack.append(v)
            DFSVisit(v)
    return cycle


if __name__ == '__main__':
    test = [[1, 5],
            [0, 2, 4, 5],
            [1, 3, 4, 5],
            [2, 4],
            [1, 2, 3, 5],
            [0, 1, 2, 4]]
    print(EulerCycle(test))
