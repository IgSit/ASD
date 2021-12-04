def correct_brackets(string):
    stack = []
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (char == '(' and last != ')') or (char == '[' and last != ']'):
                return False
    if len(stack) != 0:
        return False
    return True


if __name__ == '__main__':
    test = '[(fsf[ssf])]'
    print(correct_brackets(test))
