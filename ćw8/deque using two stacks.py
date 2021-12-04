class Deque:  # append do stack1, pop z stack2
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, x):
        self.stack1.append(x)

    def pop(self):
        if len(self.stack1) == len(self.stack2) == 0:
            print("Pop from empty deque.")
        elif len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


if __name__ == '__main__':
    test = Deque()
    test.append(3)
    test.append(5)
    test.append(7)
    print(test.pop())
