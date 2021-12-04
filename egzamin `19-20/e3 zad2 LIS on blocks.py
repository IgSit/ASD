def tower(arr):
    n = len(arr)
    func = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[j][0] <= arr[i][0] and arr[i][1] <= arr[j][1] and func[j] + 1 > func[i]:
                func[i] = func[j] + 1

    return max(func)
