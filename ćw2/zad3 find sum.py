def find_sum(arr, x):
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        curr_sum = arr[i] + arr[j]
        if curr_sum == x:
            return True
        if curr_sum > x:
            j -= 1
        if curr_sum < x:
            i += 1
    return False


if __name__ == '__main__':
    test = [2, 4, 6, 6, 7, 8, 9, 10, 44]
    print(find_sum(test, 20))
