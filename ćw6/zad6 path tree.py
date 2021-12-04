# f(i) - najlepsza wartość ścieżki zaczynającej się w wierzchołku i
# f(i) = max(0, i.val, max{f(j), j - dziecko i} + i.val)


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.best_path = None


def path(arr):

    def best_path(node):
        if node.best_path is not None:
            return node.best_path
        best_child = -1
        for child in node.children:
            best_child = max(best_child, best_path(child))
        best = max(node.val, 0, best_child + node.val)
        node.best_path = best
        return best

    return max(best_path(node) for node in arr)


if __name__ == '__main__':
    n1, n2, n3, n4, n5, n6 = Node(3), Node(5), Node(-1), Node(3), Node(-2), Node(10)
    n1.children = [n2, n3]
    n2.children = [n4]
    n3.children = [n5]
    n5.children = [n6]
    test = [n1, n2, n3, n4, n5, n6]
    print(path(test))
