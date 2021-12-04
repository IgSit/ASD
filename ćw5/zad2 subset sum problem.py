def subset_sum(nums, b_arr, target, i):
    if target == 0:
        return True
    if i < 0 or target < 0:
        return False

    if nums[i] > target:
        return subset_sum(nums, b_arr, target, i - 1)

    if isinstance(b_arr[i][target], int):
        b_arr[i][target] = subset_sum(nums, b_arr, target, i - 1) or subset_sum(nums, b_arr, target - nums[i], i - 1)

    return b_arr[i][target]


def sum_problem(nums, target):
    n = len(nums)
    b_arr = [[0 for _ in range(target + 1)] for _ in range(n)]
    for i in range(n):
        b_arr[i][0] = True
    return subset_sum(nums, b_arr, target, n - 1)


if __name__ == '__main__':
    test = [1, 4, 6, 3, 7, 9, 34]
    print(sum_problem(test, 1))