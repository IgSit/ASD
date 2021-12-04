def shortest_sequence(arr, k):
    n = len(arr)
    col_arr = [0] * k
    colours_found = 0
    i = j = 0
    shortest = n
    while j != n:
        while colours_found != k:
            if col_arr[arr[j]] == 0:
                colours_found += 1
            col_arr[arr[j]] += 1
            j += 1
            if j == n:
                break

        while colours_found == k:
            if j - i < shortest:
                shortest = j - i
            col_arr[arr[i]] -= 1
            if col_arr[arr[i]] == 0:
                colours_found -= 1
            i += 1
            if i == j:
                break

    return shortest


if __name__ == '__main__':
    test = [0, 1, 1, 1, 1, 2, 4, 4, 3, 0]
    print(shortest_sequence(test, 5))
