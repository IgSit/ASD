# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller
def ceil_index(arr, left, right, key):
    while right - left > 1:

        m = left + (right - left) // 2
        if arr[m] >= key:
            right = m
        else:
            left = m
    return right


def lis(arr, size):
    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return 0

    tail_table = [0 for _ in range(size + 1)]

    tail_table[0] = arr[0]
    length = 1
    res = []
    for i in range(1, size):

        if arr[i] < tail_table[0]:

            # new smallest value
            tail_table[0] = arr[i]

        elif arr[i] > tail_table[length - 1]:

            # A[i] wants to extend
            # largest subsequence
            tail_table[length] = arr[i]
            length += 1
            res = tail_table[:length]

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tail_table
            tail_table[ceil_index(tail_table, -1, length - 1, arr[i])] = arr[i]

    print(res)
    return length


if __name__ == '__main__':
    A = [2, 7, 3, 4, 9, 1, 8, 5]
    n = len(A)
    print(lis(A, n))
