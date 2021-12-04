def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def insertion_sort(arr, occur_arr, elem):
    n = len(arr)
    if n < 1 or arr[n - 1] < elem:
        arr.append(elem)
        occur_arr.append(1)
        return
    j = n - 1
    arr.append(0)
    occur_arr.append(0)
    while j >= 0 and arr[j] > elem:
        arr[j + 1] = arr[j]
        occur_arr[j + 1] = occur_arr[j]
        j -= 1
    arr[j + 1] = elem
    occur_arr[j + 1] = 1


def longest_incomplete(arr, k):
    n = len(arr)
    uniq_values = []
    occur = []
    uniq_found = 0
    i = j = 0
    longest = 0
    while j <= n - 1:
        while uniq_found != k:
            q = len(uniq_values)

            if q == 0 or uniq_values[q - 1] < arr[j]:
                index = -1
            else:
                index = binary_search(uniq_values, arr[j])  # O(n * log k)

            if index == -1:  # not in array
                insertion_sort(uniq_values, occur, arr[j])  # O(k * k)
                uniq_found += 1
            else:
                if occur[index] == 0:
                    uniq_found += 1
                occur[index] += 1

            if j - i + 1 > longest:
                longest = j - i + 1

            j += 1
            if j == n:
                break

        while uniq_found == k:
            index = binary_search(uniq_values, arr[i])  # O(n * log k)
            occur[index] -= 1
            if occur[index] == 0:
                uniq_found -= 1
            i += 1
            if i == j:
                break

    return longest


if __name__ == '__main__':
    test = [100, 11, 2, 2, 11, 5, 1000, 2, 11]
    print(longest_incomplete(test, 3))
