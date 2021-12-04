def bucket_radix_sort(arr):
    n = len(arr)
    max_len = max(len(arr[i]) for i in range(n))
    min_len = min(len(arr[i]) for i in range(n))
    buckets = [[] for _ in range(max_len - min_len + 1)]
    for word in arr:
        index = len(word) - min_len
        buckets[index].append(word)

    cmp_letter = max_len - 1
    curr_idx = max_len - min_len
    bucket = buckets[curr_idx]
    while cmp_letter != -1:
        counting_sort(bucket, cmp_letter)
        curr_idx -= 1
        cmp_letter -= 1
        if curr_idx >= 0:
            bucket = buckets[curr_idx] + bucket
    return bucket


def counting_sort(arr, curr_idx):
    n = len(arr)
    c_arr = [0] * 26  # each letter
    output = [0] * n

    for word in arr:
        index = ord(word[curr_idx]) - 97
        c_arr[index] += 1

    for i in range(1, 26):
        c_arr[i] += c_arr[i - 1]

    for i in range(n - 1, -1, -1):
        index = ord(arr[i][curr_idx]) - 97
        output[c_arr[index] - 1] = arr[i]
        c_arr[index] -= 1

    for i in range(n):
        arr[i] = output[i]


if __name__ == '__main__':
    test = ["sgrgfgaaa", "agrfeab", "aabrgrc", "aargrd", "bvrgrr", "dwdaagrgaa"]
    print(bucket_radix_sort(test))
