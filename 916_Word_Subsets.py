def wordSubsets(words1, words2):
    """
    :type words1: List[str]
    :type words2: List[str]
    :rtype: List[str]
    """
    tempWords = []
    for word in words1:
        fit = True
        for w in words2:
            for c in w:
                if c not in word:
                    fit = False
                    break
        if fit:
            tempWords.append(word)
    return tempWords


print(wordSubsets(["amazon", "apple", "facebook",
      "google", "leetcode"], ["lo", "eo"]))
# wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"])
