def find_min_and_max(arr):
    minimum = arr[- 1]
    maximum = arr[- 1]
    length = len(arr)
    for i in range(0, length - 1, 2):
        if arr[i] < arr[i + 1]:
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i + 1] > maximum:
                maximum = arr[i + 1]
        else:
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]
            if arr[i] > maximum:
                maximum = arr[i]
    return maximum, minimum
