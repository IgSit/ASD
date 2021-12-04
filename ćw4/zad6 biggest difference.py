def big_adjusting_difference(arr):
    max_val = max(arr)
    min_val = min(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = (max_val - min_val) / n if min_val * max_val > 0 else (max_val + abs(min_val)) / n
    for val in arr:
        index = int((val - min_val) // interval) if int((val - min_val) // interval) <= n - 1 else n - 1
        buckets[index].append(val)

    result = 0
    prev_max = max(buckets[0])
    for i in range(1, n):
        if len(buckets[i]) != 0:
            act_min = min(buckets[i])
            result = max(result, act_min - prev_max)
            prev_max = max(buckets[i])

    return result


if __name__ == '__main__':
    test = [0.54, 0.01, 0.23, 0.71, 0.51, 0.68]
    print(big_adjusting_difference(test))
