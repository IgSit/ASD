def bucket_radix_sort(arr):
    n = len(arr)
    max_len = max(len(arr[i]) for i in range(n))
    buckets = [[] for _ in range(max_len)]
    for word in arr:
        index = len(word) - 1
        buckets[index].append(word)

    curr_idx = max_len - 1
    bucket = buckets[curr_idx]
    while curr_idx != -1:
        counting_sort(bucket, curr_idx)
        curr_idx -= 1
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
    test = ["a", "ad", "b", "dd", "d", "abc"]
    print(bucket_radix_sort(test))
