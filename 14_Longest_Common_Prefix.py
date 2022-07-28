def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    #  Get the smallest:
    small = strs[0]
    for str in strs:
        small = str if len(str) < len(small) else small

    # Delete the value from the list:
    strs.remove(small)

    #  check for prefix:
    exist = True
    prefix = small
    while len(small) > 0:
        for str in strs:
            if not str.startswith(prefix):
                exist = False
                break
        if not exist:
            prefix = prefix[:-1]
            exist = True
        else:
            return prefix
    return ""


print(longestCommonPrefix(["dog", "racecar", "car"]))
