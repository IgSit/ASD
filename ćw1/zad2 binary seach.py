def binary_search(arr, i, j, x):
    if i > j:
        return None
    c = (i + j) // 2
    if arr[c] == x:
        return c
    if arr[c] > x:
        return binary_search(arr, i, c - 1, x)
    else:
        return binary_search(arr, c + 1, j, x)
