def get_area(arr, y):
    x0, y0, x1, y1 = arr
    if y1 >= y:
        return 0
    if y >= y0:
        return (x1 - x0) * (y0 - y1)
    else:  # somewhere in between y0 and y1
        return (x1 - x0) * (y - y1)


def bin_search(arr, y_min, y_max, vol, prev=0, curr=0):

    if prev < 0 < curr or curr < 0 < prev:
        no_y_between = True
        for container in arr:
            if y_min < container[1] < y_max:
                no_y_between = False
                break
        if no_y_between:
            return (y_max + y_min) / 2

    curr_vol = 0
    curr_y = (y_max + y_min) / 2
    for container in arr:
        curr_vol += get_area(container, curr_y)

    if curr_vol == vol:
        return curr_y
    if curr_vol > vol:
        return bin_search(arr, y_min, curr_y, vol, curr, curr_vol - vol)
    if curr_vol < vol:
        return bin_search(arr, curr_y, y_max, vol, curr, curr_vol - vol)


def containers(arr, vol):
    n = len(arr)
    y_min = min(arr[i][3] for i in range(n))
    y_max = max(arr[i][1] for i in range(n))

    max_vol = 0
    for container in arr:
        max_vol += get_area(container, y_max)
    if max_vol <= vol:
        return n
    else:
        y = bin_search(arr, y_min, y_max, vol)
    cnt = 0
    for container in arr:
        if y >= container[1]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    test = [[1, -1, 4, -2], [1, 3, 2, 1], [3, 5, 4, 1], [1, 5, 2, 4], [-4, 3, -1, 1]]  # x-lg, y-lg, x-pd, y-pd
    print(containers(test, 15))
