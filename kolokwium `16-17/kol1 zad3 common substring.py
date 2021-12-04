def radix_sort(arr, k):
    curr_idx = k - 1
    while curr_idx != -1:
        counting_sort(arr, curr_idx)
        curr_idx -= 1
    return arr


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


def common_substring(text, k):
    n = len(text)
    i, j = 0, k
    all_subs = []
    while j <= n:
        all_subs.append(text[i:j])
        i += 1
        j += 1
    all_subs = radix_sort(all_subs, k)
    max_reps = 0
    res = None
    i = 0
    arr_len = len(all_subs)
    while i < arr_len - 1:
        reps = 1
        while all_subs[i] == all_subs[i + 1]:
            reps += 1
            i += 1
            if reps > max_reps:
                max_reps = reps
                res = all_subs[i]
            if i == arr_len - 1:
                break
        i += 1
    return res


if __name__ == '__main__':
    print(common_substring("ababaaaaba", 3))
