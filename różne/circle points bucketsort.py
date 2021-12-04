def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j][2] < arr[i][2]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for elem in arr:
        elem.append((elem[0] ** 2 + elem[1] ** 2) ** 0.5)
        index = int((elem[2] / k) * n) if int((elem[2] / k) * n) < n else n - 1
        buckets[index].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            elem.pop()
            arr[i] = elem
            i += 1
    return arr


if __name__ == '__main__':
    test = [[1, 1], [0.5, 0.5], [0.6, 0.9], [0.4, 0.7], [0.1, 1], [0.2, 0.3]]
    print(bucket_sort(test, 2))
