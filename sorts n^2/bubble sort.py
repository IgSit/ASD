def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    print(bubble_sort([1, 5, 2, 4, 0]))
