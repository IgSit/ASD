from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cut_the_tree(main_root):

    def rec(root):
        if root.left is None and root.right is None:
            return inf

        f_l = rec(root.left) if root.left is not None else 0
        f_r = rec(root.right) if root.right is not None else 0

        return min(f_l + f_r, root.value)

    left = rec(main_root.left) if main_root.left is not None else 0
    right = rec(main_root.right) if main_root.right is not None else 0
    return left + right
