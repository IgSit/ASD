def find_leader(arr):
    n = len(arr)
    counter = 1
    leader = arr[0]
    for i in range(1, n):
        if counter == 0:
            leader = arr[i]
        if arr[i] == leader:
            counter += 1
        else:
            counter -= 1
    if counter != 0:
        check_count = 0
        for i in range(n):
            if arr[i] == leader:
                check_count += 1
            if check_count >= n // 2 + 1:
                return leader

    return None


if __name__ == '__main__':
    test = [1, 2, 1, 2, 2, 1, 3, 2, 2]
    print(find_leader(test))
