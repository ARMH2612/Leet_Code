
def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    def match(word):
        P = {}
        for x, y in zip(pattern, word):
            if P.setdefault(x, y) != y:
                return False
        return len(set(P.values())) == len(P.values())

    return filter(match, words)
    # newWords = []
    # for word in words:
    #     dictPattern = {}
    #     for cw, cp in zip(word, pattern):
    #         if cp not in dictPattern and cw not in dictPattern.values():
    #             dictPattern[cp] = cw
    #         elif cp not in dictPattern or cw not in dictPattern.values():
    #             break

    #     temp = word
    #     keys = list(dictPattern.keys())
    #     print(keys)
    #     for c in keys:
    #         word = word.replace(dictPattern[c], c, 1)
    #         print("replace ", dictPattern[c], " by ", c, " => ", word)
    #         keys.remove(c)
    #     # print('-----------------------')
    #     if word == pattern:
    #         newWords.append(temp)

    return newWords


# findAndReplacePattern(["a", "b", "c"], "a")
print(findAndReplacePattern(["abc", "cba", "xyx", "yxx", "yyx"], "abc"))
