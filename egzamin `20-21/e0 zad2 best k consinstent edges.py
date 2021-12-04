from math import inf


class Node:
    def __init__(self, left=None, leftval=0, right=None, rightval=0):
        self.left = left  # lewe podrzewo
        self.leftval = leftval  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = right  # prawe poddrzewo
        self.rightval = rightval  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.key = None


# f(i, e) - max wartość spójnego poddrzewa o korzeniu i i używające e krawędzi
# f(liść, e) = 0
# f(i, 0) = 0
# f(i, e) = max( f(i.left, e - 1) + {i, i.left}, f(i.right, e - 1) + {i, i.right},
#                max(f(i.left, e - 2 - d) + f(i.right, d) + {i, i.left} + {i, i.right}) for d in range(o, e - 2) )
# z dokładnością do e - 2 >= 0 i istnienia obydwu dzieci, jak nie ma dziecka, to wart f dziecka to 0


def valuable_tree(root, k):
    i = 0

    def rec(v):
        nonlocal i
        v.key = i
        i += 1
        if v.left:
            rec(v.left)
        if v.right:
            rec(v.right)

    rec(root)
    func = [[None for _ in range(k + 1)] for _ in range(i)]

    def fun_rec(v, e):
        if func[v.key][e] is not None:
            return func[v.key][e]
        if v.left is None and v.right is None and e > 0:
            return -inf
        if v.left is None and v.right is None:
            return 0
        if e == 0:
            return 0
        if v.left and v.right and e >= 2:
            func[v.key][e] = max(fun_rec(v.left, e - 1) + v.leftval, fun_rec(v.right, e - 1) + v.rightval)
            for d in range(0, e - 2 + 1):
                func[v.key][e] = max(func[v.key][e],
                                     fun_rec(v.left, e - 2 - d) + fun_rec(v.right, d) + v.rightval + v.leftval)
        elif v.left and v.right:
            func[v.key][e] = max(fun_rec(v.left, e - 1) + v.leftval, fun_rec(v.right, e - 1) + v.rightval)
        elif v.left:
            func[v.key][e] = fun_rec(v.left, e - 1) + v.leftval
        elif v.right:
            func[v.key][e] = fun_rec(v.right, e - 1) + v.rightval

        return func[v.key][e]

    def solve(v):
        fun_rec(v, k)
        if v.left:
            solve(v.left)
        if v.right:
            solve(v.right)

    solve(root)
    for q in range(i):
        print(func[q])
    return max(func[a][k] for a in range(i) if func[a][k] is not None)
