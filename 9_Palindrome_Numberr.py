
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # if x < 0:
    #     return False

    # res = list(map(int, str(x)))
    # i = 0
    # j = len(res)-1
    # while i < j:
    #     if res[i] != res[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True

    # Better solution :
    return str(x) == str(x)[::-1]

print(isPalindrome(0))
