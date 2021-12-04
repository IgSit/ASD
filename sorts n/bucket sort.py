def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, start, end):
    k = end - start
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int((elem - end) // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1


if __name__ == '__main__':
    test = [0.4, 0.3, 0.21, 0.37, 0.42, 0.89, 0.69, 0.7]
    bucket_sort(test, 0, 1)
    print(test)
