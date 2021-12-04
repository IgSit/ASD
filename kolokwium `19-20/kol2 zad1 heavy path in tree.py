# f(i) - najwieksza wartosc drzewa o korzeniu w i - nie moge przedluzyc do gory
# g(i) - najwieksza wartosc sciezki o poczatku i - moge przedluzyc do gory

# f(i) = max( max( f(j) + {i,j}, j - dziecko i), max( f(j) + {i,j} + f(k) +{i,k}, j,k - dzieci i), 0)
# f(liść) = 0
# g(i) = max( max( f(j) + {i,j}, j - dziecko i), 0)
# g(liść) = 0
# Rozw: max( f(i), i - wierzchołek w drzewie)


class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.func = -1
        self.g_func = -1
        self.max_so_far = -1


def heavy_path(root):

    def rec(v):
        if v.children == 0:
            v.func = 0
            v.g_func = 0
            v.max_so_far = 0
            return 0

        max0, max1 = 0, 0

        for vertex, dist in v.child:
            child_func = rec(vertex) + dist
            if child_func > max0:
                max1 = max0
                max0 = child_func
            elif child_func > max1:
                max1 = child_func

        v.func = max(max0, max0 + max1, 0)
        v.g_func = max(max0, 0)
        v.max_so_far = max(v.func, max(q.max_so_far for q, _ in v.child))
        return v.g_func

    rec(root)
    return root.max_so_far


if __name__ == '__main__':
    A, B, C, D, E, F = Node(), Node(), Node(), Node(), Node(), Node()
    A.children = 2
    A.child = [(B, 5), (C, -1)]
    B.children = 2
    B.child = [(D, 6), (E, 1)]
    C.children = 1
    C.child = [(F, 13)]
    print(heavy_path(A))
