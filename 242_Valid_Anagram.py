def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
# Faster than te second solution
    return sorted(s) == sorted(t)

#  Big time complexity
    # if len(s) == len(t):
    #     for c in s:
    #         if c in t:
    #             t = t.replace(c, '', 1)
    #             s = s.replace(c, '', 1)
    #         else:
    #             return False
    #     return True
    # return False


# Doesn't work always
    # if len(s) == len(t):
    #     temp = ['' if c in t else c for c in s]
    #     return False if len(''.join(temp)) >= 0 else True
    # return False


print(isAnagram("aacc", "ccac"))
