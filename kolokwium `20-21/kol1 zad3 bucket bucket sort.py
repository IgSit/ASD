def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, start, end):
    k = end - start
    n = len(arr)
    if n == 0:
        return arr
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int((elem - start) // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1


def bucket_o_bucket(arr, intervals):
    w = len(intervals)
    start = min(intervals[i][0] for i in range(w))
    end = max(intervals[i][1] for i in range(w))
    how_many = end - start
    division = [[] for _ in range(how_many)]
    for elem in arr:
        division[int(elem - start)].append(elem)

    i = 0
    for bucket in division:
        bucket_sort(bucket, start, start + 1)
        start += 1
        for num in bucket:
            arr[i] = num
            i += 1

    return arr
