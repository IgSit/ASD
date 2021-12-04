from random import randint


def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = partition(arr, left, right)
            if pivot - left < right - pivot:
                stack.append((pivot + 1, right))
                stack.append((left, pivot - 1))
            else:
                stack.append((left, pivot - 1))
                stack.append((pivot + 1, right))
    return arr


def partition(arr, left, right):
    rand_index = randint(left, right)
    arr[right], arr[rand_index] = arr[rand_index], arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


if __name__ == '__main__':
    test = [1, 4, 2, 6, 3, 8, 9, 3, 0, 3]
    print(quicksort(test))
