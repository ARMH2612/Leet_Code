def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    cypher = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for i in range(len(s)):
        if i+1 < len(s) and cypher[s[i]] < cypher[s[i+1]]:
            res -= cypher[s[i]]
        else:
            res += cypher[s[i]]
    return res


print(romanToInt("1994"))
