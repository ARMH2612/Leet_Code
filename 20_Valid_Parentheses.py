def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dict = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    open = []
    brackets = []
    brackets[:0] = s
    for b in brackets:
        if b in ['(', '[', '{']:
            open.append(b)

        elif b in [')', ']', '}']:
            if len(open) == 0:
                return False
            elif dict[open[len(open)-1]] != b:
                return False
            else:
                open.pop()
    return True if len(open) == 0 else False


print(isValid("(}"))
