# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     s2 = []
#     for i in range(len(s)):
#         if s[i] == ' ':
#             s2.append(' ')
#         s2.append(s[i])
#     # if(len(s2) == 1):
#     #     return 1
#     hashset = []
#     reps = []
#     count = 0
#     j = 0
#     i = 0
#     while i < len(s2):
#         c = s2[i]
#         if c not in hashset:
#             hashset.append(c)
#             count += 1
#             i += 1
#         else:
#             reps.append(count)
#             count = 0
#             hashset = []
#             i = j+1
#             j += 1
#     print(reps)
#     if reps:
#         return (max(reps))
#     else:
#         return 0


# print(lengthOfLongestSubstring(" "))

def lengthOfLongestSubstring(s):
    hashset = set()
    i, j, reps = 0, 0, 0
    for c in s:
        while c in hashset:
            hashset.remove(s[j])
            j += 1
        hashset.add(c)
        reps = max(reps, i-j+1)
        i += 1
    return reps


print(lengthOfLongestSubstring("abcabcbb"))
