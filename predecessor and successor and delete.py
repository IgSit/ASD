class BSTNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

    def display(self):
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right
    return None


def add(root, key):
    main_root = root
    while True:
        if key.key < root.key and root.left is None:
            root.left = key
            key.parent = root
            return main_root
        elif key.key < root.key:
            root = root.left
        elif key.key > root.key and root.right is None:
            root.right = key
            key.parent = root
            return main_root
        elif key.key > root.key:
            root = root.right


def find_predecessor(key):
    if key.left is not None:
        predecessor = key.left
        while predecessor.right is not None:
            predecessor = predecessor.right
        return predecessor
    else:
        predecessor = key.parent
        last = key
        while predecessor.left == last:
            predecessor = predecessor.parent
            if predecessor is None:
                return f"{key.key} is min value"
            last = last.parent
        return predecessor


def find_successor(key):
    if key.right is not None:
        successor = key.right
        while successor.left is not None:
            successor = successor.left
        return successor
    else:
        successor = key.parent
        last = key
        while successor.right == last:
            successor = successor.parent
            if successor is None:
                return f"{key.key} is max value"
            last = last.parent
        return successor


def delete_key(root, value):
    node = find(root, value)
    if node is None:
        return None

    if node.right is None and node.left is None:
        if node.parent.right == node:
            node.parent.right = None
        else:
            node.parent.left = None
        return root

    if node.right is None or node.left is None:
        child = node.right if node.right is not None else node.left
        if node.parent.right == node:
            node.parent.right = child
        else:
            node.parent.left = child
        return root

    else:
        pred = find_predecessor(node)
        node.key = pred.key
        if pred.right is None and pred.left is None:
            if pred.parent.right == pred:
                pred.parent.right = None
            else:
                pred.parent.left = None
        else:
            child = pred.right if pred.right is not None else pred.left
            if pred.parent.left == pred:
                pred.parent.left = child
            else:
                pred.parent.left = child
        return root


if __name__ == '__main__':
    r = BSTNode(20)
    test = [19, 5, 37, 35, 40, 22, 21, 23]
    for elem in test:
        r = add(r, BSTNode(elem))

    r.display()
    r = delete_key(r, 20)
    print("\n\n")
    r.display()
